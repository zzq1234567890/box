import time
import json
import re
import requests
from flask import Flask, request, redirect, Response, stream_with_context

app = Flask(__name__)

channel_cache = {}
CACHE_EXPIRE = 100

def fetch_authorized_url(channel_id):
    print(f"[FETCH] Requesting new authorized URL for channel: {channel_id}")
    api = 'https://beesports.net/authorize-channel'
    payload = json.dumps({
        "channel": f"https://live_tv.starcdnup.com/{channel_id}/index.m3u8"
    })
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://beesports.net',
        'referer': 'https://beesports.net/live-tv',
    }

    try:
        response = requests.post(api, data=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'channels' in data and data['channels']:
            print(f"[FETCH] Received authorized URL: {data['channels'][0]}")
            return data['channels'][0]
    except Exception as e:
        print(f"[ERROR] fetch_authorized_url: {e}")
    return None

@app.route('/proxy')
def proxy():
    original_url = request.args.get('url')
    channel_id = request.args.get('id')

    if not original_url:
        return "Missing 'url' parameter", 400

    print(f"[PROXY] Incoming request for channel: {channel_id}")
    print(f"[PROXY] Requested URL: {original_url}")


    if channel_id:
        now = time.time()
        cache_entry = channel_cache.get(channel_id)
        age = now - cache_entry['timestamp'] if cache_entry else float('inf')

        if not cache_entry or age > CACHE_EXPIRE:
            print("[CACHE] Cache expired or missing. Refreshing authorization...")
            new_url = fetch_authorized_url(channel_id)
            if not new_url:
                return "Failed to refresh authorized URL", 500
            channel_cache[channel_id] = {
                'url': new_url,
                'timestamp': now
            }

 
    if original_url.endswith('.m3u8') and channel_id:
        url = channel_cache[channel_id]['url']
    else:
        url = original_url

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://p.m82xg4z0cdbz7.com/',
        'Origin': 'https://p.m82xg4z0cdbz7.com',
        'Accept': '*/*'
    }

    try:
        resp = requests.get(url, headers=headers, stream=True)
        resp.raise_for_status()
        content_type = resp.headers.get('Content-Type', 'application/octet-stream')


        if 'application/vnd.apple.mpegurl' in content_type or url.endswith('.m3u8'):
            print("[PROXY] Detected M3U8 file. Rewriting TS paths...")
            content = resp.text
            base_url = url.rsplit('/', 1)[0]
            lines = content.split('\n')
            new_lines = []

            for i, line in enumerate(lines):
                if line.startswith('#EXTINF'):
                    new_lines.append(line)
                    next_line = lines[i + 1] if i + 1 < len(lines) else ''
                    if next_line and not next_line.startswith('#'):
                        ts_url = f"{base_url}/{next_line}" if not next_line.startswith('http') else next_line
                        proxied_url = f"{request.host_url.rstrip('/')}/proxy?url={ts_url}&id={channel_id}"
                        new_lines.append(proxied_url)
                elif line.startswith('#EXTM3U') or line.startswith('#EXT-X') or line.startswith('#EXT-X-PROGRAM-DATE-TIME'):
                    new_lines.append(line)

            rewritten = '\n'.join(new_lines)
            response = Response(rewritten, content_type="application/vnd.apple.mpegurl")
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Cache-Control'] = 'no-store'
            return response

        # TS 文件流式返回
        stream_response = Response(
            stream_with_context(resp.iter_content(chunk_size=1024)),
            content_type=content_type,
            status=resp.status_code
        )
        stream_response.headers['Access-Control-Allow-Origin'] = '*'
        return stream_response

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Proxy request failed: {e}")
        return f"Error proxying request: {str(e)}", 500

@app.route('/')
def index():
    channel_id = request.args.get('id')
    if not channel_id:
        return "Missing 'id' parameter", 400

    now = time.time()
    cache_entry = channel_cache.get(channel_id)
    age = now - cache_entry['timestamp'] if cache_entry else float('inf')

    if not cache_entry or age > CACHE_EXPIRE:
        print("[INDEX] Refreshing authorization...")
        new_url = fetch_authorized_url(channel_id)
        if not new_url:
            return "Failed to fetch authorized URL", 500
        channel_cache[channel_id] = {
            'url': new_url,
            'timestamp': now
        }

    master_url = channel_cache[channel_id]['url']
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://p.m82xg4z0cdbz7.com/',
        'Origin': 'https://p.m82xg4z0cdbz7.com',
        'Accept': '*/*'
    }

    try:
        master_resp = requests.get(master_url, headers=headers)
        master_resp.raise_for_status()
        master_content = master_resp.text
        lines = master_content.split('\n')

        sub_path = None
        for line in lines:
            if line and not line.startswith('#'):
                sub_path = line.strip()
                break

        if not sub_path:
            return "No sub-playlist found in master M3U8", 500

        base_url = master_url.rsplit('/', 1)[0]
        sub_url = f"{base_url}/{sub_path}" if not sub_path.startswith('http') else sub_path
        print(f"[INDEX] Sub-playlist URL: {sub_url}")

        sub_resp = requests.get(sub_url, headers=headers)
        sub_resp.raise_for_status()
        sub_content = sub_resp.text
        sub_lines = sub_content.split('\n')
        sub_base = sub_url.rsplit('/', 1)[0]

        new_lines = []
        for i, line in enumerate(sub_lines):
            if line.startswith('#EXTINF'):
                new_lines.append(line)
                next_line = sub_lines[i + 1] if i + 1 < len(sub_lines) else ''
                if next_line and not next_line.startswith('#'):
                    ts_url = f"{sub_base}/{next_line}" if not next_line.startswith('http') else next_line
                    proxied_url = f"{request.host_url.rstrip('/')}/proxy?url={ts_url}&id={channel_id}"
                    new_lines.append(proxied_url)
            elif line.startswith('#EXTM3U') or line.startswith('#EXT-X') or line.startswith('#EXT-X-PROGRAM-DATE-TIME'):
                new_lines.append(line)

        playlist = '\n'.join(new_lines)
        response = Response(playlist, content_type="application/vnd.apple.mpegurl")
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Cache-Control'] = 'no-store'
        return response

    except Exception as e:
        print(f"[ERROR] Failed to process M3U8: {e}")
        return f"Error processing M3U8: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

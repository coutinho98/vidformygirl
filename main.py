import os
from yt_dlp import YoutubeDL
from urllib.parse import urlparse

url = input("URL: ")
dir = './videos'
os.makedirs(dir, exist_ok=True)

if not url.startswith(('http://', 'https://')):
    print('URL inválida')
    exit(1)

ydl_opts = {
    'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[vcodec^=avc1]',
    'outtmpl': os.path.join(dir, '%(title)s.%(ext)s'),
    'noplaylist': True,
    'merge_output_format': 'mkv',
    'restrictfilenames': True,
    'writesubtitles': True,
    'subtitlelangs': ['en', 'pt-br'],
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mkv',
    }],
    'progress_hooks': [lambda d: print(f"Progresso: {d['_percent_str']} (frag {d.get('fragment_index', 0)}/{d.get('fragment_count', 'desconhecido')})") if d['status'] == 'downloading' else None],
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"baixado: {info['title']} em {info.get('height', 'resolução desconhecida')}p")
except Exception as e:
    print(f"Error: {e}")
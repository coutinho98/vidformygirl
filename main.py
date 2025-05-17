from yt_dlp import YoutubeDL
from urllib.parse import urlparse

url = input(": ")

if not url.startswith(('http://', 'https://')) or 'youtube' not in urlparse(url).netloc:
    print('URL inválida ou não é do YouTube')
    exit(1)

ydl_opts = {
    'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[vcodec^=avc1]',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True,
    'merge_output_format': 'mkv',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mkv',
    }],
    'progress_hooks': [lambda d: print(f"Progresso: {d['downloaded_bytes'] / d['total_bytes'] * 100:.1f}%") if d['status'] == 'downloading' else None],
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"baixado: {info['title']} em {info.get('height', 'resolução desconhecida')}p")
except Exception as e:
    print(f"Error: {e}")
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
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"baixado: {info['title']} em {info.get('resolução', 'bad resolution')}")
except Exception as e:
    print(f"Error: {e}")
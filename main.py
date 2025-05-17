from yt_dlp import YoutubeDL

url = input(": ")
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
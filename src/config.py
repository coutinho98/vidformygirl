import os

baseDirectory =  os.path.dirname(os.path.abspath(__file__))
videoDirectory = os.path.join(baseDirectory, '..', 'video')
audioDirectory = os.path.join(baseDirectory, '..', 'audio')

os.makedirs(videoDirectory, exist_ok=True)
os.makedirs(audioDirectory, exist_ok=True)

baseOptions = {
    'noplaylist': True,
    'progress_hooks': [lambda d: print(f"Progresso: {d['_percent_str']} (frag {d.get('fragment_index', 0)}/{d.get('fragment_count', 'desconhecido')})") if d['status'] == 'downloading' else None],
}

videoOptions = {
    **baseOptions,
    'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[vcodec^=avc1]',
    'outtmpl': os.path.join(videoDirectory, '%(title)s.%(ext)s'),
    'merge_output_format': 'mkv',
    'writesubtitles': True,
    'subtitlelangs': ['en', 'pt-br'],
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mkv',
    }],
}

audioOptions = {
    **baseOptions,
    'format': 'bestaudio[ext=m4a]/bestaudio',
    'outtmpl': os.path.join(audioDirectory, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
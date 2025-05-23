import os

baseDirectory =  os.path.dirname(os.path.abspath(__file__))
videoDirectory = os.path.join(baseDirectory, '..', 'video')
audioDirectory = os.path.join(baseDirectory, '..', 'audio')

os.makedirs(videoDirectory, exist_ok=True)
os.makedirs(audioDirectory, exist_ok=True)

baseOptions = {
    'noplaylist': True,
    'progress_hooks': [lambda d: print(f"Progress: {d['_percent_str']} (frag {d.get('fragment_index', 0)}/{d.get('fragment_count', 'desconhecido')})") if d['status'] == 'downloading' else None],
}

videoOptions = {
    **baseOptions,
    'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[vcodec^=avc1]',
    'outtmpl': os.path.join(videoDirectory, '%(title)s.%(ext)s'),
    'merge_output_format': 'mkv',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mkv',
    }],
}

videoOptionsMP4 = {
    **baseOptions,
    'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[vcodec^=avc1]',
    'outtmpl': os.path.join(videoDirectory, '%(title)s.%(ext)s'),
    'merge_output_format': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
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
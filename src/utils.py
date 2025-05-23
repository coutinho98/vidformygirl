from urllib.parse import urlparse

def validateURL(url):
    return url.startswith(('http://', 'https://'))

def getFileName(info):
    return f"{info['title']}.{info.get('ext', 'mkv')}"
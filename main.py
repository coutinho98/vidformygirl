from src.downloader import downloadVideoMKV, downloadVideoMP4, downloadAudio

def main():
    url = input("URL: ")
    print("1. Vídeo (MKV)")
    print("2. Vídeo (MP4)")
    print("3. Áudio (MP3)")
    choice = input("Escolha (1-3): ")

    if choice == '1':
        print(downloadVideoMKV(url))
    elif choice == '2':
        print(downloadVideoMP4(url))
    elif choice == '3':
        print(downloadAudio(url))

if __name__ == "__main__":
    main()
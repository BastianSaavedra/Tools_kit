from pytube import YouTube
import os, platform


def menu():
    loop = True
    while loop:
        print("Youtube Downloader")
        print("1. Download Mp4(highest quality)")
        print("2. Download Mp4(lowest quality)")
        print("3. Download Mp3")
        print("4. Close")

        option = input("Choose an options (1/2/3): ")

        if option == '1' or option == '2' or option == '3':
            url = input("Paste the url: ")
            download(option, url)
        else:
            print("Program Finished")
            loop = False


# Find the operative system and return main path
def system():
    so = platform.system()
    if so == "Windows":
        return 'C://'
    elif so == "Linux":
        return '/'


def find_download_folder(directory_base=system()):
    try:
        for current_path, directories, files in os.walk(directory_base):
            if 'Downloads' in directories:
                return os.path.join(current_path, 'Downloads')
            elif 'Descargas' in directories:
                return os.path.join(current_path, 'Descargas')
    except Exception as e:
        print(f"Error {str(e)}")
    return None


def download(option, url):
    yt = YouTube(url)
    path = find_download_folder()
    print("Title", yt.title)

    if option == '1':
        video_high_quality = yt.streams.get_highest_resolution()
        video_high_quality.download(output_path=path)
        print("Download mp4 Complete")
    elif option == '2':
        video_low_quality = yt.streams.get_lowest_resolution()
        video_low_quality.download(output_path=path)
    elif option == '3':
        mp3 = yt.streams.get_audio_only()
        mp3.download(output_path=path)
    
    print(f"Download {yt.title} completed!")
    print(f"Saved at {path}")


if __name__ == "__main__":
    menu()


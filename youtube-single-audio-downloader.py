
from pytube import Playlist, YouTube
from urllib.parse import urlparse
link = input("Enter YouTube single URL: ")

def uri_validator(urlLink):
    try:
        result = urlparse(urlLink)
        return all([result.scheme, result.netloc])
    except:
        return False
    
if (uri_validator(link.split('&')[0])):
    yt_single = YouTube(link)

    def on_progress(stream, chunk, bytes_remaining):
        global inc, my_progress, label2
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        inc = int(percentage_of_completion)
        print("size", total_size / 1024 / 1024, "MB")
        print("downloaded:", bytes_downloaded / 1024 / 1024, "MB, ", inc, "%")

    yt_single.register_on_progress_callback(on_progress)
    yt_single.streams.filter(only_audio=True).get_audio_only().download(
        "C:/Users/Purushottam/Documents/projects/youtubeVideoDownloader/youtubeAudio")
    print("Video Downloaded: ", yt_single.title)

    print("\ndownloaded.")
else:
    print("provided url is not valid")

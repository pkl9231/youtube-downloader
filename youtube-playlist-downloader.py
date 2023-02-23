from pytube import Playlist, YouTube

type = input("You want to download playlist or single video, enter -> 'list' or 'single' : ")


if(type == "list"):
  link = input("Enter YouTube Playlist URL: ")

if(type == "single"):
  link = input("Enter YouTube URL: ")

yt_playlist = Playlist(link)

yt_single = YouTube(link)

format = input("Input type to download -> video or audio    :")


def on_progress(stream, chunk, bytes_remaining):
    global inc, my_progress, label2
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    inc = int(percentage_of_completion)
    print("size", total_size / 1024 / 1024)
    print("downloaded:", bytes_downloaded / 1024 / 1024 , "MB, ", inc , "%")


if (format == "video" and type == "list"):
    for video in yt_playlist.videos:
        video.register_on_progress_callback(on_progress)
        video.streams.get_highest_resolution().download(
            "C:/Users/Purushottam/Documents/projects/youtubeVideoDownloader/youtubeVideo")
        print("Video Downloaded: ", video.title)

if (type == "audio" and type == "list"):
    for audio in yt_playlist.videos:
        audio.register_on_progress_callback(on_progress)
        audio.streams.filter(only_audio=True).get_audio_only().download(
            "C:/Users/Purushottam/Documents/projects/youtubeVideoDownloader/youtubeAudio")
        print("Video Downloaded: ", audio.title)

if (format == "video" and type == "single"):
    yt_single.register_on_progress_callback(on_progress)
    yt_single.streams.get_highest_resolution().download(
        "C:/Users/Purushottam/Documents/projects/youtubeVideoDownloader/youtubeVideo")
    print("Video Downloaded: ", yt_single.title)

if (format == "audio" and type == "single"):
    yt_single.register_on_progress_callback(on_progress)
    yt_single.streams.filter(only_audio=True).get_audio_only().download(
        "C:/Users/Purushottam/Documents/projects/youtubeVideoDownloader/youtubeAudio")
    print("Video Downloaded: ", yt_single.title)

print("\nAll downloaded.")

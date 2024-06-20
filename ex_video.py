from pytube import YouTube


def download_video(url, output_path='video.mp4'):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(filename=output_path)

# https://youtu.be/fLeJJPxua3E

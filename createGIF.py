import subprocess
import os


def create_srt(subtitles, srt_path):
    def format_time(seconds):
        ms = int((seconds - int(seconds)) * 1000)
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02},{ms:03}"

    with open(srt_path, 'w', encoding='utf-8') as file:
        for i, subtitle in enumerate(subtitles, start=1):
            start_time = format_time(subtitle['start'])
            end_time = format_time(subtitle['end'])
            text = subtitle['text']
            file.write(f"{i}\n{start_time} --> {end_time}\n{text}\n\n")


def create_gif(video_path, subtitles, start_time, duration, output_path):
    srt_path = 'temp_subtitles.srt'
    create_srt(subtitles, srt_path)

    clipped_video_path = "clipped_video.mp4"
    subprocess.run([
        'ffmpeg',
        '-ss', str(start_time),
        '-t', str(duration),
        '-i', video_path,
        '-c', 'copy',
        clipped_video_path,
        '-y'
    ])

    video_with_subs_path = "video_with_subs.mp4"
    font_size = 24
    subprocess.run([
        'ffmpeg',
        '-i', clipped_video_path,
        '-vf', f"subtitles={srt_path}:force_style='Fontsize={font_size}, Backgroundcolor=black'",
        '-c:a', 'copy',
        video_with_subs_path,
        '-y'
    ])

    subprocess.run([
        'ffmpeg',
        '-i', video_with_subs_path,
        '-vf', 'fps=10,scale=320:-1:flags=lanczos',
        output_path,
        '-y'
    ])

    os.remove(clipped_video_path)
    os.remove(video_with_subs_path)
    os.remove(srt_path)

    print(f"GIF saved to {output_path}")

# Create subtitle file for GIFs

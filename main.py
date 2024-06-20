from ex_audio import extract_audio
from ex_video import download_video
from script_audio import transcription
from createGIF import create_gif
from script_audio import create_subtitle_file
import os


phrases = [
    
    "I don't care how much money you make.",
    "your success is dependent upon how you use the 24.",
    "You only get 24 hours in a day."
]

subtitles = create_subtitle_file(transcription)

for text in subtitles:
    print(text['text'])

for phrase in phrases:

    for subtitle in subtitles:
        if phrase in subtitle["text"]:
            print(subtitle["text"])
            start_time = subtitle["start"]
            end_time = subtitle["end"]
            duration = end_time - start_time

    output_file = f'{phrase}.gif'  # Example output file name
    sub_list = [{'start': 0, 'end': duration, 'text': phrase}]

    create_gif('video.mp4', sub_list, start_time, duration, output_file)

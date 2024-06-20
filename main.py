from ex_audio import extract_audio
from ex_video import download_video
from script_audio import transcription
from createGIF import create_gif
from script_audio import create_subtitle_file
import os



phrases = []  #list to store all user selected phrases from the transcript

subtitles = create_subtitle_file(transcription)   
i=-1 

for text in subtitles:
    i = i + 1
    print( str(i) + text['text'])


input_string = input("Enter a list of indexes separated by spaces: ")

input_list = list(map(int, input_string.split()))

for selection in input_list:
    phrases.append(subtitles[selection]['text'])


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

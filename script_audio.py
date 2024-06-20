import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.wav", word_timestamps=True)
transcription = result
print("Transcript created")
# with open('transcript.txt', 'w', encoding='utf-8') as f:
#         f.write(f"{result}")


def create_subtitle_file(text):

    subtitles = []
    for segment in result["segments"]:
        subtitles.append({
            "start" : segment["start"],
            "end" : segment["end"],
            "text": segment["text"]
        })
        # with open('subtitles.txt', 'w', encoding='utf-8') as f:
        #         f.write(str(subtitles) + '\n')
        
    return subtitles

# create_subtitle_file(transcription)



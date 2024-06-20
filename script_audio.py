import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.wav")
transcription = result
print("Transcript created")



def create_subtitle_file(text):

    subtitles = []
    for segment in result["segments"]:
        subtitles.append({
            'start' : segment['start'],
            'end' : segment['end'],
            'text': segment['text']
        })
        
    return subtitles





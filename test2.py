import os
import subprocess
import wave
import json
import srt
from vosk import Model, KaldiRecognizer
from datetime import timedelta

def extract_audio(video_path, audio_path):
    subprocess.run(['ffmpeg', '-i', video_path, '-ac', '1', '-ar', '16000', audio_path, '-y'])

def transcribe_audio(audio_path, model_path='model'):
    wf = wave.open(audio_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Audio file must be WAV format mono PCM.")

    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    results.append(json.loads(rec.FinalResult()))

    return results

def seconds_to_timedelta(seconds):
    return timedelta(seconds=seconds)

def create_srt(transcription, srt_path):
    subtitles = []
    index = 1

    for result in transcription:
        if 'result' in result:
            for word in result['result']:
                start = seconds_to_timedelta(word['start'])
                end = seconds_to_timedelta(word['end'])
                text = word['word']
                subtitles.append(srt.Subtitle(index, start, end, text))
                index += 1

    with open(srt_path, 'w', encoding='utf-8') as f:
        f.write(srt.compose(subtitles))

def main(video_path, output_srt_path):
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)
    transcription = transcribe_audio(audio_path)
    create_srt(transcription, output_srt_path)
    os.remove(audio_path)

if __name__ == "__main__":
    video_path = 'video.mp4'
    output_srt_path = 'output.srt'
    main(video_path, output_srt_path)
    print(f"SRT file saved to {output_srt_path}")

import ffmpeg


def extract_audio(video_path, audio_path='audio.wav'):
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, format='wav', acodec='pcm_s16le', ac=1, ar='16000')
        .run(overwrite_output=True)
    )

# extract_audio('video.mp4')
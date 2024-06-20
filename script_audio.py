# from youtube_transcript_api import YouTubeTranscriptApi
#
#
# # Example function to get transcript from YouTube video
# def transcribe_youtube_video(video_id):
#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         full_text = ' '.join([line['text'] for line in transcript])
#         return full_text
#     except Exception as e:
#         print(f"Error fetching transcript: {str(e)}")
#         return None
#
#
# # Replace 'VIDEO_ID' with the actual ID of the YouTube video
# video_id = 'fLeJJPxua3E'
# transcription = transcribe_youtube_video(video_id)
# # print(transcription)
import whisper

model = whisper.load_model("medium")
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
    return subtitles



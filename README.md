# ytVideo-to-GIF
Youtube video segments to gif conversion with subtitle using audio transcript with whisper.




1. Run the ex_video.py file and uncomment the call of the function, give your video link as the argument
2. video.mp4 file will be created
3. Now extract audio from it using ex_audio.py extract_audio function call
4. audio.wav file will be created, this file will be used for transcription using th whisper base model (used "base" for speed, for more accuracy use "medium")
5. Run the main.py file

A list of phrases are displayed 
![phrase list](/images/phraselist.jpg)

The user is prompted to select the phrases with its index

![phrase list](/images/phraselist.jpg)


Corresponding GIFs are created and saved in the creared_gifs directory

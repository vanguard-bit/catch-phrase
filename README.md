Have you ever thought you'd like to see all instances of catch-phrases one character says....... all at once?

[For example "How Cute" from Kaguya-Sama: Love is War](MergedOutput.mp4)
or the same in japnese



This codebase uses subtitles to search for the catch-phrases using "pysubs2" library(subtitles in srt format)
and "moviepy" to clip the videos(videos in mp4)

change '^(.*)?(it\'s|it\'s a|quite|how|very|really) (cute).*?$' in main.py with your catch.phrase and it should work
Still in beta stages


TODO:
Doucmentation
Make it more user friendly
Support for subtitles format and also other video formats
Support for movies and series along with anime
Create a branch and use ffmpeg and its python wrapper to improve video quality


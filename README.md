# Telegram Youtube Screenshot and Video downloader Bot<br />
Youtube link: https://www.youtube.com/watch?v=aoTyZXChcIA <br />
[![IMAGE VIDEO](https://img.youtube.com/vi/aoTyZXChcIA/0.jpg)](https://www.youtube.com/watch?v=aoTyZXChcIA)<br />

## What can This Telegram Bot do?
- Make Screenshots of a Youtube video at a specific time 
command: `/scr ytlink 00:00:10` will download a snapshot of your videolink (ytlink) at 10 sec (hh:mm:ss)

- Download a specific part of the youtube video as MP4 
command: `/vid ytlink 00:00:10 00:00:05` will download a part if the video (ytlink) starting at 10 seconds with a movielength of 5 seconds

- Download the full video is best video and audio quality
command: `/dl ytlink` wil download the full youtube video

The results will be sent on telegram (if not to big) and stored in a local `vid` or `img` folder

## Setup 
- Clone this repository `git clone https://github.com/raspiuser1/Youtube-Screenshot-and-Video-Downloader` 
- Install the packages: `pip install -r requirements.txt`
- Get a key from @thebotfather on telegram and store it in the key.txt file
- Start the bot with `python3 snap.py`
You can view the commands of this bot by typing `/help'

## 
If you do not have the possibility you can use the webpage link in the video description. Its a web-based bot.

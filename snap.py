#thetube.selfhost.co/snap?=1
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram
import sys
import time
import os
import re
from os.path import basename, splitext
import logging
from datetime import date
from datetime import datetime
from os import path
import io
import random
import subprocess
import random


my_token=open("key.txt").readline().rstrip()
#store plain txt in:
txtfile = ""

updater = Updater(my_token,use_context=True)
bot = telegram.Bot(token=my_token)


remove1 = True        
        

def unknown_text(update: Update, context: CallbackContext):
    #uncomment if need to send to telegram:
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
    print("Sorry I can't recognize you , you said '%s'")
    
def help(update: Update, context: CallbackContext):
    update.message.reply_text(""" ======Options Youtube Screenshot Bot======
/restart - restart bot

/stop - stops the bot (start manually)

/scr - Screenshot [link] [time]
- fill in the youtube link and the time (hh:mm:ss)

/dl - [link] [+ for remove] download video in high quality mp4 file

/vid - [link] [starttime] [duration] Send a part of the youtube video
- fill in the youtube link, the start time (hh:mm:ss) and duration time of the video (hh:mm:ss)

""")

def restart(update: Update, context: CallbackContext):
    try:
        update.message.reply_text("Restarting...")
        p = subprocess.Popen("./restart.sh", stdout=subprocess.PIPE, shell=True)
    finally:
        sys.exit()
        
def stop(update: Update, context: CallbackContext):
    try:
        updater.dispatcher.bot.sendMessage(chat_id=update.message.chat_id, text="Bot will be stopped (start manually)")
        p = subprocess.Popen("./stop.sh", stdout=subprocess.PIPE, shell=True)
    finally:
        sys.exit()

def makedir():
        isExist = os.path.exists(os.getcwd() + "/vid/")
        if not isExist:
                os.makedirs(os.getcwd() + "/vid/")
        isExist = os.path.exists(os.getcwd() + "/img/")
        if not isExist:
                os.makedirs(os.getcwd() + "/img/")           
            
def remove_snap(update: Update, context: CallbackContext):
    global remove1
    if remove1:
        remove1 = False
        update.message.reply_text("Remove snapshots after processing Disabled")
    else:
        remove1 = True
        update.message.reply_text("Remove snapshots after processing Enabled")
    
def unknown(update: Update, context: CallbackContext):
    #update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)
    print("Onbekend commando")    
    

                
def get_yt_vid(update: Update, context: CallbackContext):
    global videoid,filenu88     
    try:
        wt = update.message.text.split(" ")
        ytlink = str(wt[1])
        try:
            pre = str(wt[2])
        except Exception:
            pre = "-"           


        if "youtu" in ytlink and "http" in ytlink:
                if "youtube.com/watch?v=" in ytlink:
                    videoid = ytlink.split("youtube.com/watch?v=")[1]
                if "youtu.be" in ytlink:
                    videoid = ytlink.split("youtu.be/")[1]
                
        utime = int(time.time())

        filenu88 = os.getcwd() + "/vid/" + videoid + "_" + str(date.today()) + "_" + str(utime) + ".mp4"        

        update.message.reply_text("Downloading video in High Quality....")
        

        cmd = subprocess.Popen(f"youtube-dl -o {filenu88} -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' https://www.youtube.com/watch?v={videoid}",
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = cmd.communicate()


        if cmd.returncode == 0 :
            msgnu77 = "Download succes"
            update.message.reply_text(msgnu77)
            print(msgnu77)
            try:
                updater.dispatcher.bot.send_video(chat_id=update.message.chat_id, video=open(filenu88, 'rb'))                
                if os.path.isfile(filenu88) and pre == "+":
                    os.remove(filenu88)
            except Exception:
                    print("File is to big to send, check the local vid folder")   
                    update.message.reply_text("File is to big to send, check the local vid folder")                 
        else:
            print("Fail")
            update.message.reply_text("Failed to get video")
    except:
        update.message.reply_text("Error: Fill in all the arguments")                
  
def set_welcome(update: Update, context: CallbackContext): 
    update.message.reply_text("Screenshot bot started")
  
            
def vid(update: Update, context: CallbackContext):
    global videoid,filenu88,sec1     
    try:
        wt = update.message.text.split(" ")
        ytlink = str(wt[1])
        time1 = str(wt[2])
        time2 = str(wt[3])
        
        if "youtu" in ytlink and "http" in ytlink:
                if "youtube.com/watch?v=" in ytlink:
                    videoid = ytlink.split("youtube.com/watch?v=")[1]
                if "youtu.be" in ytlink:
                    videoid = ytlink.split("youtu.be/")[1]
                
        utime = int(time.time())
        filenu88 = os.getcwd() + "/vid/" + videoid + "_" + str(date.today()) + "_" + str(utime) + ".mp4"

        update.message.reply_text("Getting videopart....")
        

        cmd = subprocess.Popen(f"ffmpeg $(youtube-dl -g 'https://www.youtube.com/watch?v={videoid}' | sed 's/^/-ss '{time1}' -i /') -t '{time2}' -strict -2 -c copy {filenu88}",
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = cmd.communicate()


        if cmd.returncode == 0 :
            msgnu77 = "succes"
            update.message.reply_text(msgnu77)
            print(msgnu77)
            try:
                updater.dispatcher.bot.send_video(chat_id=update.message.chat_id, video=open(filenu88, 'rb'))
            except Exception:
                update.message.reply_text("File is to big to send, check the local vid folder")
        else:
            print("Fail")
            update.message.reply_text("Failed to get Video")
    except:
        update.message.reply_text("Error: Fill in all the arguments")




def screenshot(update: Update, context: CallbackContext):
    global videoid,filenu88,sec1     
    try:
        wt = update.message.text.split(" ")
        ytlink = str(wt[1])
        sec1 = str(wt[2])
        
        if "youtu" in ytlink and "http" in ytlink:
                if "youtube.com/watch?v=" in ytlink:
                    videoid = ytlink.split("youtube.com/watch?v=")[1]
                if "youtu.be" in ytlink:
                    videoid = ytlink.split("youtu.be/")[1]
                
        utime = int(time.time())
        filenu88 = os.getcwd() + "/img/" + videoid + "_" + str(date.today()) + "_" + str(utime) + ".jpg"

        update.message.reply_text("Getting image....")
        
        try:
            cmd = subprocess.Popen(f'ffmpeg -ss "{sec1}" -i $(youtube-dl -f 137 --get-url "https://www.youtube.com/watch?v={videoid}") -vframes 1 -q:v 2 "{filenu88}"',
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = cmd.communicate()
        except Exception:
            cmd = subprocess.Popen(f'ffmpeg -ss "{sec1}" -i $(youtube-dl -f 22 --get-url "https://www.youtube.com/watch?v={videoid}") -vframes 1 -q:v 2 "{filenu88}"',
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = cmd.communicate()

        if cmd.returncode == 0 :
            msgnu77 = "succes: " + ytlink + "\t" + filenu88 + " @ (HH:MM:SS):" + sec1
            update.message.reply_text(msgnu77)
            print(msgnu77) 
            updater.dispatcher.bot.send_photo(chat_id=update.message.chat_id, photo=open(filenu88, 'rb'))
                        
            if os.path.isfile(filenu88) and remove1:
                os.remove(filenu88)
        else:
            print("Fail")
            update.message.reply_text("Fail to get screenshot")
    except:
        update.message.reply_text("Error: Fill in all the arguments")
  

#telegram options=================================================================================================
makedir()
updater = Updater(my_token,use_context=True)
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('restart', restart))
updater.dispatcher.add_handler(CommandHandler('scr', screenshot))
updater.dispatcher.add_handler(CommandHandler('vid', vid))
updater.dispatcher.add_handler(CommandHandler('dl', get_yt_vid))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('rem', remove_snap))
updater.dispatcher.add_handler(CommandHandler('welcome', set_welcome, pass_args=True))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling(timeout=600)    
#updater.dispatcher.bot.sendMessage(chat_id=update.message.chat_id, text="Snapshot bot started")



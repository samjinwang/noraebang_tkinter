# Made by Tae-Hwan Kim
# Codable Project Team
# University of Illinois at Urbana Champaign
# Title: Home Noraebang Player
# main.py

from tkinter import *
from tkinter import font
# import pytube
import buttonMethod as bm
# import imageio
# from PIL import Image, ImageTk
# import os
# import time
# from threading import *
from appMaterials import *
#
# # from PIL import ImageTk, Image
# # from pathlib import Path
# # from moviepy.editor import *
# # from moviepy.video.fx.resize import resize
# # import pygame


# ################################
# # Call methods from buttonMethod
# ################################
def uT():
    bm.urlType(urlEntry,playList)

def uTAhead():
    bm.urlTypeAhead(urlEntry,playList)

def startVideoButton():
    bm.startVideo(win,playList)

def cancelReserve():
    bm.cancelReservation(win,playList)

def cancelButton():
    bm.cancelMusic()

# ################################
# # Application Window Settings
# ################################
win = AppWindow("1200x800","Home Noraebang").set() #Application window

fixedSys25 = FontStyle("FixedSys",25).set() #Font for buttons
arial19 = FontStyle("Arial",19).set() #Font for Url Type Entry box
arial11 = FontStyle("Arial",11).set() #Font for the title above Url Entry

urlLabel = Labels(win, "Youtube URL:",arial11,800,11) #Title above url Entry


urlEntry = Entries(win, arial19, 800,40).set() #Entry where you type youtube URL


playList = Lists(win,800,170,40,22).set() #The text box where you can see what songs have been reserved


####### Buttons & Corresponding Methods #######
reserve = Buttons(win,'예약',fixedSys25,800,90).set()
reserve.config(command = uT)

reserveAhead = Buttons(win,'우선예약',fixedSys25,1000,90).set()
reserveAhead.config(command = uTAhead)

cancel = Buttons(win,'취소',fixedSys25,1000,600).set()

cancelReservation = Buttons(win,'예약취소',fixedSys25,1000,680).set()
cancelReservation.config(command = cancelReserve)

start = Buttons(win,'시작',fixedSys25,800,600).set()
start.config(command = startVideoButton)

pause = Buttons(win,'일시정지',fixedSys25,800,680).set()
pitchUP = Buttons(win,'#',fixedSys25,50,600).set()
pitchDown = Buttons(win,'♭',fixedSys25,50,680).set()
male = Buttons(win,'남자키',fixedSys25,230,600).set()
female = Buttons(win,'여자키',fixedSys25,230,680).set()
revUP = Buttons(win,'에코업',fixedSys25,410,600).set()
revDown = Buttons(win,'에코다운',fixedSys25,410,680).set()
spdUP = Buttons(win,'템포업',fixedSys25,590,600).set()
spdDown = Buttons(win,'템포다운',fixedSys25,590,680).set()

#Activate the application window
win.mainloop()
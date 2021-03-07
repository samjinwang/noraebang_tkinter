from tkinter import *
from tkinter import font
import pytube
import buttonMethod as bm
from PIL import Image, ImageTk

# from PIL import ImageTk, Image
# from pathlib import Path
# from moviepy.editor import *
# from moviepy.video.fx.resize import resize
# import pygame

urlList = []

################################
# Call methods from buttonMethod
################################
# def uT():
#     bm.urlType(urlEntry,musicList)


################################
# Application Window Settings
################################

win = Tk()  # construct a window

# Window Setting
win.geometry("1200x800")
win.title("Home Noraebang")  # Title of the window
fixedSys25 = font.Font(family ="FixedSys", size = 25)  # Font and Font size
arial19 = font.Font(family ="Arial", size = 19)


# 입력창(URL 입력)
urlEntry = Entry(win,font = arial19, bd = 2)
urlEntry.pack()
urlEntry.place(x=800,y=40)





videoLabel = Label(win)
videoLabel.pack()


# def urlType():
#     url = urlEntry.get()  # a is the thing typed in the entry
#     youtube = pytube.YouTube(url)
#     video = youtube.streams.first()
#     video.download()
#     name = youtube.streams[0].title
#     musicList.insert(END,name +"\n")

    # print(str(Path().absolute()))

#URL Label:
var = StringVar()
urlLabel = Label(win,font = font.Font(family ="Arial", size = 11), textvariable = var)
var.set("Youtube URL:")
urlLabel.pack()
urlLabel.place(x=800, y=11)

#Music List
musicList = Text(win, height = 22, width = 40)
musicList.pack()
musicList.place(x=800, y = 170)

########### buttons ############

def urlType():
    url = urlEntry.get()  # a is the thing typed in the entry
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download()
    name = youtube.streams[0].title
    musicList.insert(END,name +"\n")

#예약
reserve = Button(win, text='예약', font = fixedSys25)  # construct a button
reserve.pack()  # put a button on the window
reserve.place(x=800, y=90)
reserve.config(width=8, height=1)  # button size
reserve.config(command= urlType)  # execute the function of reserve



#우선예약
reserveAhead = Button(win, text='우선예약', font = fixedSys25)  # construct a button
reserveAhead.pack()  # put a button on the window
reserveAhead.place(x=1000, y=90)
reserveAhead.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button


# start
start = Button(win,font = fixedSys25, text='시작')  # construct a button
start.pack()  # put a button on the window
start.place(x=800, y=600)
start.config(width=8, height=1)  # button size
#reserve.config(command=startVideo)  # execute the function of button # # # video = imageio.get_reader(video_name)

# def startVideo(label):
#
#     for image in video.iter_data():
#         frame_image = ImageTk.PhotoImage(Image.fromarray(image))
#         label.config(image=frame_image)
#         label.image = frame_image
#         time.sleep(0.025)



# delay = int(1000 / video.get_meta_data()['fps'])
#
# def stream(label):
#     try:
#         image = video.get_next_data()
#     except:
#         video.close()
#         return
#     label.after(delay, lambda: stream(label))
#     frame_image = ImageTk.PhotoImage(Image.fromarray(image))
#     label.config(image=frame_image)
#     label.image = frame_image
#
# videoLabel.after(delay,lambda: stream(videoLabel) )




#cancel
cancel = Button(win, text='취소', font = fixedSys25)  # construct a button
cancel.pack()  # put a button on the window
cancel.place(x=1000, y=600)
cancel.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

#cancel reserve
cancelReserve = Button(win, text='예약취소', font = fixedSys25)  # construct a button
cancelReserve.pack()  # put a button on the window
cancelReserve.place(x=1000, y=680)
cancelReserve.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

# # pause
pause= Button(win,font = fixedSys25, text='일시정지')  # construct a button
pause.pack()  # put a button on the window
pause.place(x=800, y=680)
pause.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button


# # pitch up
pitchUP = Button(win,font = fixedSys25, text='#')  # construct a button
pitchUP.pack()  # put a button on the window
pitchUP.place(x=50, y=600)
pitchUP.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

# # pitch down
pitchDown = Button(win,font = fixedSys25, text='♭')  # construct a button
pitchDown.pack()  # put a button on the window
pitchDown.place(x=50, y=680)
pitchDown.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

# # male pitch
male = Button(win,font = fixedSys25, text='남자키')  # construct a button
male.pack()  # put a button on the window
male.place(x=230, y=600)
male.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

# # female pitch
female = Button(win,font = fixedSys25, text='여자키')  # construct a button
female.pack()  # put a button on the window
female.place(x=230, y=680)
female.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

# # reverb up
revUp = Button(win,font = fixedSys25, text='에코업')  # construct a button
revUp.pack()  # put a button on the window
revUp.place(x=410, y=600)
revUp.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

# # reverb down
revDown = Button(win,font = fixedSys25, text='에코다운')  # construct a button
revDown.pack()  # put a button on the window
revDown.place(x=410, y=680)
revDown.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button
#
# #speed up
spdUp= Button(win,font = fixedSys25, text='탬포업')  # construct a button
spdUp.pack()  # put a button on the window
spdUp.place(x=590, y=600)
spdUp.config(width=8, height=1)  # button size
#reserve.config(command=urlType)  # execute the function of button

# #speed down
spdDown = Button(win,font = fixedSys25, text='탬포다운')  # construct a button
spdDown.pack()  # put a button on the window
spdDown.place(x=590, y=680)
spdDown.config(width=8, height=1)  # button size
# #reserve.config(command=urlType)  # execute the function of button



win.mainloop()  # Execute the window


# import tkinter as tk, threading
# import imageio
# import os
# import time
# from PIL import Image, ImageTk
#
# print (os.getcwd())
#
# video_name = "[TJ노래방] 사랑이었나봐 - 기리보이  TJ Karaoke"+".mp4" #This is your video file path
# video = imageio.get_reader(video_name)
#

#
#
# if __name__ == "__main__":
#
#     root = tk.Tk()
#     my_label = tk.Label(root)
#     my_label.pack()
#     my_label.place(x=50, y=50)
#     thread = threading.Thread(target=stream, args=(my_label,))
#     thread.daemon = 1
#     thread.start()
#     root.mainloop()

import numpy as np
import cv2
import time

# cap = cv2.VideoCapture('[TJ노래방] 사랑이었나봐 - 기리보이  TJ Karaoke.mp4')
# i=0 #frame counter
# frameTime = 1 # time of each frame in ms, you can add logic to change this value.
# while(cap.isOpened()):
#     ret = cap.grab() #grab frame
#     i=i+1 #increment counter
#     if i % 3 == 0: # display only one third of the frames, you can change this parameter according to your needs
#         ret, frame = cap.retrieve() #decode frame
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(100) & 0xFF == ord('q'):
#             break
#     #time.sleep(24)
# cap.release()
# cv2.destroyAllWindows()
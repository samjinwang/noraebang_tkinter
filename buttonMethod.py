#made by: Tae-Hwan Kim
#Codable project team
#University of Illnois at Urbana Champaign

import pytube
from tkinter import *
import imageio
from PIL import Image, ImageTk
import time
from threading import Thread,Event
import moviepy.editor as mp
from pygame import mixer


urlList = [] #store URLs typed
musicList = [] #store the title of songs downloaded from the given URLS


def urlType(urlEntry,playList): #youtube URL 값들만 추가될수 있도록 해야함
    """
    Method for reserve button
    When the Url is typed in the Entry
    store it so the song from the given URL will be ready to be played later

    :param urlEntry: type(tkinter.Entry())
    :param playList: type(tkinter.Text())
    :return:
    """
    url = urlEntry.get()  # a is the thing typed in the entry
    urlEntry.delete(0, 'end')
    if 'https://youtu.be/' in url or 'youtube.com/'in url:
        urlList.append(url) #store url in the list

    youtube = pytube.YouTube(url) #search the correspondding video on Youtube
    videoName = youtube.streams[0].title #Get the title of the song
    filterName = videoName.replace('/','') #This prevent the error. The str "/" vanishes when the song is downloaded.
    newName = filterName.replace('Feat.', 'Feat')
    musicList.append(newName) #Append the title of video in the list
    playList.delete('1.0', END) #clear the app play list before show every song reserved
    for music in musicList:
        playList.insert(END,music +"\n") #show all titles of songs on the application window

def urlTypeAhead(urlEntry,playList):
    """
    Method for reserveAhead button

    When the Url is typed in the Entry
    store it at the beginning so the song from to the given URL will be ready to play next

    :param urlEntry: type(tkinter.Entry())
    :param playList: type(tkinter.Text())
    :return:
    """
    url = urlEntry.get()  # a is the thing typed in the entry
    urlEntry.delete(0, 'end')
    if 'https://youtu.be/' in url or 'youtube.com/' in url:
        urlList.insert(0, url) #store url in the list
    youtube = pytube.YouTube(url) #search the correspondding video on Youtube
    videoName = youtube.streams[0].title #Get the title of the song
    filterName = videoName.replace('/', '')  # This prevent the error. The str "/" vanishes when the song is downloaded.
    newName = filterName.replace('Feat.', 'Feat')
    musicList.insert(0, newName) #store the title of video in the list at the first place
    playList.delete('1.0', END) #clear the app play list before show every song reserved
    for music in musicList:
        playList.insert(END,music +"\n") #show all titles of songs on the application window

def screenGenerator(label):
    """
    Method for startVideo method below and start button
    Cut the video into many frames

    :param label: type(tkinter.Label()) -> where the video will be
    :return:
    """
    youtube = pytube.YouTube(urlList[0])
    video = youtube.streams.first()
    video.download()
    videoname = musicList[0]+'.mp4'
    downloadedVideo = imageio.get_reader(videoname)

    clip = mp.VideoFileClip(musicList[0] + '.mp4')
    clip.audio.write_audiofile(musicList[0] + '.mp3')
    mixer.music.load(musicList[0] + '.mp3')

    buffer = 0 # 1초당 30프레임. if buffer = 30, 음악파일 1초 늦게 시작
    for image in downloadedVideo.iter_data():
        buffer +=1
        if buffer == 5:
            mixer.music.play()
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
        time.sleep(0.025)


def startVideo(win,playList):
    """
    start the video on the application

    :param win: type(tkinter.TK())
    :param playList: type(tkinter.Text())
    :return:
    """

    videoLabel = Label(win)
    thread = Thread(target=screenGenerator, args=(videoLabel,))
    videoLabel.pack()
    videoLabel.place(x=50, y=50)
    thread.daemon = 1
    thread.start()

    playList.delete('1.0', END)

    for i in range(1,len(musicList)):
        playList.insert(END, musicList[i] + "\n")



def cancelMusic(): #파일삭제까지 추가해야함
    stop = Event()
    stop.clear()
    # del(urlList[0])
    # del(musicList[0])
    # playList.delete('1.0', END)
    # for music in musicList:
    #     playList.insert(END,music +"\n")

def cancelReservation(playList):
    """
    remove the reserved song which is supposed to be played next

    :param win: type(tkinter.TK())
    :param playList: type(tkinter.Text())
    :return:
    """
    del(urlList[0])
    del(musicList[0])
    playList.delete('1.0', END)
    for music in musicList:
        playList.insert(END,music +"\n")




# def urlTypeAhead():
#     url = urlEntry.get()  # a is the thing typed in the entry
#     urlList.insert(0, url)
#     youtube = pytube.YouTube(url)
#     videoName = youtube.streams[0].title
#     newName = videoName.replace('/','')
#     musicList.insert(0, newName)
#     playList.delete('1.0', END)
#     for music in musicList:
#         playList.insert(END,music +"\n")
#     print(musicList)


#
#
# def screenGenerator(label):
#     youtube = pytube.YouTube(urlList[0])
#     video = youtube.streams.first()
#     video.download()
#     videoname = musicList[0]+'.mp4'
#     downloadedVideo = imageio.get_reader(videoname)
#
#
#     for image in downloadedVideo.iter_data():
#         frame_image = ImageTk.PhotoImage(Image.fromarray(image))
#         label.config(image=frame_image)
#         label.image = frame_image
#         time.sleep(0.025)
#

#
#     playList.delete('1.0', END)
#     for i in range(1,len(musicList)):
#         playList.insert(END, musicList[i] + "\n")
#
#     # if thread.is_alive():
#

# #
# # def cancelMusic(): #파일삭제까지 추가해야함
# #     if thread.is_alive():
# #         running_event.clear()
# #         thread.join()
# #
# #     del(urlList[0])
# #     del(musicList[0])
# #     playList.delete('1.0', END)
# #     for music in musicList:
# #         playList.insert(END,music +"\n")
# #     print(musicList)


# def cancelReservation():
#     del(urlList[0])
#     del(musicList[0])
#     playList.delete('1.0', END)
#     for music in musicList:
#         playList.insert(END,music +"\n")



#
# ########### buttons ############
#
# def urlType(): #youtube URL 값들만 추가될수 있도록 해야함
#     url = urlEntry.get()  # a is the thing typed in the entry
#     urlList.append(url)
#     youtube = pytube.YouTube(url)
#     videoName = youtube.streams[0].title
#     newName = videoName.replace('/','')
#     musicList.append(newName)
#     playList.delete('1.0', END)
#     for music in musicList:
#         playList.insert(END,music +"\n")
#     print(musicList)
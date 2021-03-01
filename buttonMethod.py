import pytube
from tkinter import *

def urlType(urlEntry,musicList):
    url = urlEntry.get()  # a is the thing typed in the entry
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download()
    name = youtube.streams[0].title
    musicList.insert(END,name +"\n")


# 예약 명을 리스트에 담는다
# 우선예약은 리스트 0번으로
# 예약 리스트에 포함된거와 앱에서 표시되는 예약 리스트는 별개
# 예약 버튼은 유투브 타이틀 추가 및 다운
# 영상을 시작할때 유투브 영상이 다운되면서 플레이가 되는식으로
# 영상이 완료되면 영상 삭제
# 취소버튼도 영상 삭제
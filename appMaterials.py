#Made by Tae-Hwan Kim
#This python file is for the application setting

from tkinter import *
from tkinter import font

class AppWindow:
    """
    Main window setting

    :param size: The main window size - "width x height" ex) "1200x800"
    :param appTitle: The main window title (str)
    :return: application window (type - tkinter.Tk())
    """
    def __init__(self,size, appTitle):
        self.size = size
        self.appTitle = appTitle

    def set(self):
        app = Tk()
        app.geometry(self.size) #Window size
        app.title(self.appTitle) #window Title

        return app

class FontStyle:
    """
    Font setting

    :param fontType: font type (str) ex) "Arial", "Times New Roman"
    :param fontSize: font size (int)
    :return: (type - tkinter.Font())
    """
    def __init__(self, fontType, fontSize):
        self.fontType = fontType
        self.fontSize = fontSize

    def set(self):
        fnt = font.Font(family=self.fontType, size=self.fontSize)

        return fnt

class Buttons:
    """
    Button settings

    :param application: the window where button is located (type - tkinter.Tk())
    :param buttonName: button Name (str)
    :param fontStyle: fontStyle (tk.Font())
    :param x_coor: x coordinate of a button (int)
    :param y_coor: y coordinate of a button (int)
    :return: (type - tkinter.Button())
    """
    def __init__(self,application,buttonName,fontsytle,x_coor,y_coor):
        self.application = application
        self.buttonName = buttonName
        self.fontsytle = fontsytle
        self.x_coor = x_coor
        self.y_coor = y_coor

    def set(self):
        btn = Button(self.application, text=self.buttonName, font=self.fontsytle)
        btn.pack() #Activate Button
        btn.place(x=self.x_coor, y= self.y_coor) #Location
        btn.config(width=8, height=1) #Size -> fixed

        return btn


class Labels:
    """
    Label settings -> Any text on the application

    :param application: the window where button is located (type - tkinter.Tk())
    :param labelName: label Name (str)
    :param fontStyle: fontStyle (tk.Font())
    :param x_coor: x coordinate (int)
    :param y_coor: y coordinate (int)
    :return: (type - tkinter.Label())
    """
    def __init__(self, application, labelName, fontsytle, x_coor, y_coor):
        self.application = application
        self.labelName = labelName
        self.fontsytle = fontsytle
        self.x_coor = x_coor
        self.y_coor = y_coor

    def set(self):
        var = StringVar()
        label = Label(self.application, text=self.labelName, font=self.fontsytle)
        var.set(self.labelName)
        label.pack()
        label.place(x=self.x_coor, y=self.y_coor)

        return label


class Entries:
    """
    Entry Setting -> it will be where you type your URLs

    :param application: the window where button is located (type - tkinter.Tk())
    :param fontStyle: fontStyle (tk.Font())
    :param x_coor: x coordinate (int)
    :param y_coor: y coordinate (int)
    :return: (type - tkinter.Entry())
    """
    def __init__(self, application, fontsytle, x_coor, y_coor):
        self.application = application
        self.fontsytle = fontsytle
        self.x_coor = x_coor
        self.y_coor = y_coor

    def set(self):
        entry = Entry(self.application, font=self.fontsytle, bd=2)
        entry.pack()
        entry.place(x=self.x_coor, y=self.y_coor)

        return entry


class Lists:
    """
    List: Text box in the application.
    It will be used to display what songs have been reserved.

    :param application: the window where button is located (type - tkinter.Tk())
    :param x_coor: x coordinate (int)
    :param y_coor: y coordinate (int)
    :param widthVal: width size (int)
    :param heightVal: height size (int)
    :return: (type - tkinter.Text())
    """
    def __init__(self, application, x_coor, y_coor, widthVal, heightVal):
        self.application = application
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.widthVal = widthVal
        self.heightVal = heightVal

    def set(self):
        textWindow = Text(self.application, width=self.widthVal, height=self.heightVal)
        textWindow.pack()
        textWindow.place(x=self.x_coor, y=self.y_coor)

        return textWindow
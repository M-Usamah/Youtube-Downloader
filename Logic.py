import pytube
from tkinter import messagebox
import os
import earthpy as et
Home = et.io.HOME
saveToFile = Home + '\Downloads'
saveFiles = os.path.join(saveToFile)
saveFile = os.chdir(saveFiles)
saveFile
def video(dowlink,dowFile = saveFile):
    dowFile
    try:
        yt = pytube.YouTube(dowlink)
        Stream = yt.streams.filter(progressive=True,file_extension='mp4').last()
        try:
            Stream.download()
            messagebox._show("Done","Video is downloaded")
        except Exception as down:
                messagebox.showerror("error","Can't connect to Net")
    except Exception as link:
        messagebox.showerror("error",'Enter a correct Link')

def Playlist(dowlink, downfile = saveFile):
    downfile
    try:
        yt = pytube.Playlist(dowlink)
        for videos in yt.videos:
            try:
                videos.streams.filter(progressive=True,file_extension='mp4').last().download()
            except Exception as down:
                messagebox.showerror("error","Can't connect to Net")
        messagebox._show("Done","Playlist is downloaded")
    except Exception as link:
        messagebox.showerror("error",'Enter a correct Link')

if __name__ == "__main__":
    video("https://youtu.be/1XEZBKvo5Uc")

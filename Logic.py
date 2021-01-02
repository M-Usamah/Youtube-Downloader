import pytube
from tkinter import messagebox
import os

def video(dowlink,d = os.chdir("/home/evildevil127/Downloads")):
    
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

def Playlist(dowlink, d = os.chdir("/home/evildevil127/Downloads")):
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
    # os.chdir("/home/evildevil127/Downloads")
    print(os.getcwd())
    video("https://youtu.be/1XEZBKvo5Uc")


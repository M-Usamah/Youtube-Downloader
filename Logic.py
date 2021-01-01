import pytube
import os

def video():
    dowlink = input("Enter a link to download vidoe: ")
    try:
        yt = pytube.YouTube(dowlink)
        showName = yt.title
        print(showName)
        Stream = yt.streams.filter(progressive=True,file_extension='mp4').last()
        Stream.download()
    except Exception as link:
        print('Error...\nEnter a correct Link')

def Playlist():
    dowlink = input("Enter a link to download full playlist: ")
    yt = pytube.Playlist(dowlink)
    print(yt.title)
    for videos in yt.videos:
        videos.streams.filter(progressive=True,file_extension='mp4').last().download()


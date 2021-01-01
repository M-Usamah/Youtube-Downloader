import pytube

dowlink = input("Enter a vidoe link to download: ")
try:
    yt = pytube.YouTube(dowlink)
    showName = yt.title
    print(showName)
    Stream = yt.streams.filter(progressive=True,file_extension='mp4').last()
    Stream.download()
except Exception as link:
    print('Error...\nEnter a correct Link')
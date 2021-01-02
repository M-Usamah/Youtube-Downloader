from tkinter import *
import Logic



class gui:

    def __init__(self, root):
        self.homePage(root)

    def homePage(self, root):
        root.minsize(500, 500)
        root.maxsize(500, 500)
        self.mainframe = Frame(root, bg='crimson', width=500, height=500)
        self.mainframe.pack(fill=BOTH, expand=TRUE)

        navframe = Frame(self.mainframe, bg='#1C1C1C', height=30, width=500)
        navframe.pack(side=TOP, fill=X)

        topMainFrame = Frame(self.mainframe, bg='crimson')
        topMainFrame.pack(side=TOP, fill=X, pady=10)

        ytdownlable = Label(topMainFrame, text="Youtube Downloder",
                            font="cursive 30 bold", fg="black", bg='crimson')
        ytdownlable.pack(side=TOP, fill=BOTH, expand=1)

        self.centerMainFrame = Frame(self.mainframe, bg='crimson')
        self.centerMainFrame.pack(side=TOP, fill=BOTH, expand=1)

        self.centenVideoFrame = Frame(self.mainframe, bg='crimson')
        self.centenPlayFrame = Frame(self.mainframe, bg='crimson')

        self.mainPage(self.centerMainFrame)
        self.vidoePage(self.centenVideoFrame)
        self.playlistPage(self.centenPlayFrame)

        bottomMainFrame = Frame(
            self.mainframe, bg='#1c1c1c', height=10, width=500)
        bottomMainFrame.pack(side=BOTTOM, fill=X)

    def mainPage(self, root):

        textLable = Label(root, text="What do you want to download",
                          font='cursive 15 bold', fg="black", bg='Crimson')
        textLable.place(x=110, y=50)

        self.option = ['Vidoe', 'Playlist']
        self.lists = StringVar()
        self.lists.set(self.option[0])

        optionbox = OptionMenu(root, self.lists, *self.option)
        optionbox.place(x=205, y=90)

        self.continueButton = Button(root, text="Continue", command=lambda: [
                                     self.continueButtonFunction()])
        self.continueButton.place(x=205, y=200)

    def vidoePage(self, root):

        textLabel = Label(root, text="Enter a youtube video link you want to Download",
                          font='cursive 12 bold', fg="black", bg='Crimson')
        textLabel.place(x=89, y=50)

        self.videoEnterBox = Entry(root, width=43, font='cursive', fg='blue', bg='gray')
        self.videoEnterBox.place(x=100, y=90,)

        downloadButton = Button(root, text="Download", command = lambda:[self.vidoePageFunction()])
        downloadButton.place(x=205, y=150)

        self.homeButton(root)

    def playlistPage(self, root):

        textLabel = Label(root, text="Enter a youtube Playlist link you want to Download",
                          font='cursive 12 bold', fg="black", bg='Crimson')
        textLabel.place(x=89, y=50)

        self.playEnterBox = Entry(root, width=43, font='cursive', fg='blue', bg='gray')
        self.playEnterBox.place(x=100, y=90,)

        downloadButton = Button(root, text="Download", command = lambda:[self.playlistPageFunction()])
        downloadButton.place(x=205, y=150)

        self.homeButton(root)

    def playlistPageFunction(self):
        linkBox = self.playEnterBox.get()
        link = str(linkBox)
        Logic.Playlist(link)

    def vidoePageFunction(self):
        linkBox = self.videoEnterBox.get()
        link = str(linkBox)
        Logic.video(link)

    def continueButtonFunction(self):
        
        if self.lists.get() == self.option[0]:
            self.swapFrame(self.centenVideoFrame)

        elif self.lists.get() == self.option[1]:
            self.swapFrame(self.centenPlayFrame) 

        else:
            pass

    def swapFrame(self, frameName):
        self.centerMainFrame.forget()
        self.centenVideoFrame.forget()
        self.centenPlayFrame.forget()
        frameName.tkraise()
        frameName.pack(side=TOP, fill=BOTH, expand=1)

    def homeButton(self, root):

        homeButton = Button(root, text="Home", width=8, command=lambda: [
                            self.homeButtonFunction(self.centerMainFrame)])
        homeButton.place(x=205, y=200)

    def homeButtonFunction(self, frameName):
        self.centenVideoFrame.forget()
        self.centenPlayFrame.forget()
        frameName.tkraise()
        frameName.pack(side=TOP, fill=BOTH, expand=1)


if __name__ == "__main__":

    root = Tk()
    gui(root)
    root.mainloop()

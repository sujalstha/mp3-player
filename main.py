from tkinter import *
from pygame import *
from tkinter import PhotoImage
import os

font = ('Times', 15)


def playSong():
    current_song = playlist.get(ACTIVE)
    print("Music Playing", current_song)
    mixer.music.load(current_song)
    song_status.set("Playing")
    mixer.music.play()


def stopSong():
    song_status.set("Stopped")
    mixer.music.stop()
    print("Music Stopped")


def pauseSong():
    song_status.set("Paused")
    mixer.music.pause()
    print("Music Paused")


def resumeSong():
    song_status.set("Resume")
    mixer.music.unpause()
    print("Music Resumed")


def playbackSong():
    song_status.set("Song Played Back")
    mixer.music.rewind()
    print("Music Played Back")


win = Tk()
icon_img = PhotoImage(file='mp3-flat.png')
win.title("Mp3 player v.1")
win.iconphoto(False, icon_img)

mixer.init()
song_status = StringVar()
song_status.set("scrolling")

playlist = Listbox(win,
                   selectmode=SINGLE,
                   bg='cyan',
                   fg="black",
                   font=font,
                   width=20)
playlist.grid(columnspan=6)

os.chdir(r'C:\Users\User\PycharmProjects\mp3\test songs')
directory = os.listdir()

for songs in directory:
    playlist.insert(END, songs)

# Play Button
play_btn = Button(win, text="play", command=playSong)
play_btn.config(font=font,
                bg='white',
                fg='black',
                padx=7,
                pady=7)
play_btn.grid(row=1, column=0)

# Stop Button
stop_btn = Button(win, text="stop", command=stopSong)
stop_btn.config(font=font,
                bg='white',
                fg='black',
                padx=7,
                pady=7)
stop_btn.grid(row=1, column=2)

# Pause Button
pause_btn = Button(win, text="pause", command=pauseSong)
pause_btn.config(font=font,
                 bg='white',
                 fg='black',
                 padx=7,
                 pady=7)
pause_btn.grid(row=1, column=3)

# Resume Song
resume_btn = Button(win, text="resume", command=resumeSong)
resume_btn.config(font=font,
                  bg='white',
                  fg='black',
                  padx=7,
                  pady=7)
resume_btn.grid(row=1, column=4)


# Rewind Song
rewind_btn = Button(win, text="rewind", command=playbackSong)
rewind_btn.config(font=font,
                  bg='white',
                  fg='black',
                  padx=7,
                  pady=7)
rewind_btn.grid(row=1, column=5)

win.mainloop()

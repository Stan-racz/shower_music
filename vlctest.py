import vlc
import os, random


quit = 0

def songPath(song):
    songPath = "/home/pi/douche/songs/" + song + ".mp3"
    return songPath

def songPathRandom(song):
    songPath = "/home/pi/douche/songs/" + song
    return songPath

def randomSong():
    test = random.choice(os.listdir("/home/pi/douche/songs"))
    return test

while(quit==0):
    
    choice = input("Enter action : ")
    if choice == "play":
        song = input("Enter song name : ")
        player = vlc.MediaPlayer(songPath(song))
        player.play()
    
    elif choice == "pause":
        player.pause()
    
    elif choice == "stop":
        player.stop()
    
    elif choice == "random":
        #if player.is_running == True:
            #player.stop
        player = vlc.MediaPlayer(songPathRandom(randomSong()))
        player.play()
    elif choice == "quit":
        quit=1
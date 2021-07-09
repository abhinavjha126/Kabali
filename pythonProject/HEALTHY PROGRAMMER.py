from pygame import mixer
from datetime import datetime
from time import time

def gettime():
    return (f"[{datetime.now()}]")
def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        query = input()
        if query == stopper:
            mixer.music.stop()
            break
def log(status):
    with open("Records of Water,Eye,Physical.txt", "a") as f:
        f.write(f"{gettime()} : {status}" + "\n")

if __name__=='__main__':
    int_water = time()
    int_eye = time()
    int_exercise = time()
    waterexe = 10
    eyeexe = 25
    physicalexe = 35
    while True:
        if (time() - int_water) > waterexe:
            print("PLEASE DRINK WATER AND OFF THE MUSIC")
            print("PRESS --------DRANK------- to STOP:")
            musicloop("water.mp3", "DRANK")
            print("Water Successfully Drank\n")
            int_water = time()
            log("WATER DRANK")

        if (time() - int_eye) > eyeexe:
            print("PLEASE DO EYES EXERCISE AND STOP THE MUSIC")
            print("PRESS --------EYDONE------- to STOP:")
            musicloop("eye.mp3", "EYDONE")
            print("Eyes Exercise Successfully Done\n")
            int_eye = time()
            log("EYE EXERCISE DONE")

        if (time() - int_exercise) > physicalexe:
            print("PLEASE DO PHYSICAL EXERCISE AND STOP THE MUSIC")
            print("PRESS --------EXDONE------- to STOP:")
            musicloop("physical.mp3", "EXDONE")
            print("Physical Exercise Successfully Done\n")
            int_exercise = time()
            log("PHYSICAL EXERCISE DONE")

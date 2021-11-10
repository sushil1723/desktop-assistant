from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
        break

def log_msg(msg):
    with open("schedule.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    init_water=time()
    init_exercise=time()
    init_eyes=time()
    init_food=time()
    watersec=60
    exercisesec=90*60
    eyessec=40*60
    foodsec=180*60

    while True:
        if time()-init_water > watersec:
            print("water drinking time. enter 'd' to stop the alarm")
            musiconloop("water.mp3" , "d")
            init_water=time()
            log_msg("water drank at")
        if time()-init_exercise > exercisesec:
            print("exercise time. enter 'e' to stop the alarm")
            musiconloop("exercise.mp3" , "d")
            init_exercise=time()
            log_msg("exercise done  at")    
        if time()-init_eyes > eyessec:
            print("eyes exercise time. enter 'ey' to stop the alarm")
            musiconloop("eyes.mp3" , "d")
            init_eyes=time()
            log_msg("eyes exercise done at")
        if time()-init_food > foodsec:
            print("food time. enter 'f' to stop the alarm")
            musiconloop("food.mp3", "d")
            init_food=time()
            log_msg("ate at")
    
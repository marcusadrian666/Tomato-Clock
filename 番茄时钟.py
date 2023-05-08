import time
from playsound import playsound

def pomodoro_timer():
    while True:
        print("工作25分钟")
        playsound('sound.mp3')
        time.sleep(1500)
        print("休息5分钟")
        playsound('sound.mp3')
        time.sleep(300)

pomodoro_timer()

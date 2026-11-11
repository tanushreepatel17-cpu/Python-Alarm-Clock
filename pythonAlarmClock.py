#python alarm clock

import time
import datetime
import pygame

#creating func with set_alarm as parameter alarm_time
#alarm_time is the time entered by the user
def set_alarm(alarm_time):

    #display the time for which alarm is set
    print(f"alarm set for {alarm_time}")

    #store the audio file name
    sound_file = "alarm.mp3"

    #bbolean variable to control the while loop
    is_running = True

    #Run the loop until alarm is triggered
    while is_running:

        #get current system time in HH:MM:SS format
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        #display current time in terminal
        print(current_time)

        #campare current time with user enterd alarm time
        if current_time == alarm_time:
            print("WAKE UP! ")

            #initialize pygame mixer to play audio
            pygame.mixer.init()
            #load the alarm sound file
            pygame.mixer.music.load(sound_file)
            #play the alarm sound
            pygame.mixer.music.play()

            #wait until the sound finishes playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            #stop the main loop after a;arm rings
            is_running = False

        #wait for 1 second before checking time again
        time.sleep(1)

if __name__ == "__main__":
    #taking input from user for alarm time
    alarm_time = input("enter the alarm time (HH:MM:SS): ")

    #call the alarm set function 
    set_alarm(alarm_time)
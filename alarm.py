from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the alarm to be set in 24-hour format: HH:MM:SS\n")
alarm_hour= alarm_time[0:2]
alarm_minutes= alarm_time[3:5]
alarm_seconds= alarm_time[6:8]

print(f"Your alarm is set for {alarm_time}")

while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    if (alarm_hour == current_hour):
        if (alarm_minutes == current_minutes):
            if (alarm_seconds == current_seconds):
                print("Wake Up!!!")
                playsound('alarm0.mp3')   
                break
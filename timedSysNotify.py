import schedule
import time
import os

def job():
    os.system('notify-send "hello from python file" "cool notification"')

if __name__ == "__main__":
    schedule.every().day.at("19:19").do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)





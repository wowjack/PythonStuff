#opens up my intro cybersecurity class zoom meeting
#every mwf at 1:25pm

import webbrowser, schedule, time, setproctitle

def job():
    webbrowser.open("https://udel.zoom.us/j/91235825201")



if __name__ == "__main__":
    setproctitle.setproctitle("CyberSec-login-script")

    schedule.every().monday.wednesday.friday.at("13:24").do(job)

    while True:
        schedule.run_pending()
        time.sleep(30)

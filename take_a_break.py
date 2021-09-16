import time
import webbrowser

repeatitionTime = 3
timesRun = 0
print("Enjoy the moment - Anurag ;)")

while(timesRun < repeatitionTime):
    webbrowser.open_new("https://www.google.co.in/")
    time.sleep(0.2)
    timesRun = timesRun + 1

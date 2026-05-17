import time,subprocess
time_left=60
while time_left>0:
    print(time_left)
    time.sleep(1)
    time_left-=1

subprocess.run(['start','alarm.wav'],shell=True)


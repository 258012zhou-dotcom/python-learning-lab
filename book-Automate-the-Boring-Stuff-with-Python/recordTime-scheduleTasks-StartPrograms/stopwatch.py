import time

print('press enter to begin and to mark laps. Ctrl-C quits')
input()
print('started')
start_time=time.time()
last_time=start_time
lap_number=1

try:
    while True:
        input()
        lap_time=round(time.time()-last_time,2)
        total_time=round(time.time()-start_time,2)
        print(f'lap {lap_number}: {total_time}({lap_time})',end='')
        lap_number+=1
        last_time=time.time()
except KeyboardInterrupt:
    print('\nDone')
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        # timer = '{:02d}:{:02d}'.format(mins, secs)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end = '\r')
        time.sleep(1)
        t -= 1
    print('Lift off!')

t = int(input('Enter the time in seconds: '))
countdown(t)
from time import sleep


def Time_Count(seconds):
    while seconds:
        minute, sec = divmod(seconds, 60)
        count = '{:2d}min : {:2d}sec'.format(min, sec)
        print(count, end='\r')
        sleep(1)
        seconds -= 1


Time_Count()

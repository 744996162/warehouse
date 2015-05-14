__author__ = 'Administrator'

import thread
from time import sleep, ctime


def loop0():
    print ("start loop0 at:", ctime())
    sleep(4)
    # loop1()
    print("loop0 done at:", ctime())
    pass


def loop1():
    print ("start loop1 at:", ctime())
    sleep(2)
    print("loop 1 done at:", ctime())
    pass

def main():
    print ("starting at :", ctime())
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print("all done at:", ctime())
    pass

if __name__=="__main__":
    main()

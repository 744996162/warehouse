from time import sleep, ctime
import threading

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


def test():
    print ("starting at :", ctime())
    loop0()
    loop1()
    print("all done at:", ctime())
    pass


if __name__=="__main__":
    test()
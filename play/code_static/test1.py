#ecoding=utf-8

import os
import os.path



class Foo(object):
    val = 0

    def __init__(self):
       self.val = 1

if __name__ == '__main__':
    foo = Foo()
    print foo.val
    print Foo.val

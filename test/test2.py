__author__ = 'Administrator'


def foo (n):
    return lambda i:  n + i

t =foo(5)
print t
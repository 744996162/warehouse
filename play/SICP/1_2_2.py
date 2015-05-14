__author__ = 'Administrator'
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    pass

def fibonacci2(n):
    a=1
    b=0
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        for i in range(n-1):
            temp=a
            a=a+b
            b=temp
        return a



if __name__ == '__main__':
    # t=fibonacci(40)
    t2=fibonacci2(64)
    # t2=factorial2(6)
    # print(t,t2)
    print(t2)
    pass
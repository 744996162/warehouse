__author__ = 'Administrator'
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    pass

def factorial2(n):
    temp=1
    for i in range(1,n):
        temp=temp*i
    return temp

if __name__ == '__main__':
    t=factorial(10)
    t2=factorial2(6)
    print(t,t2)
    pass
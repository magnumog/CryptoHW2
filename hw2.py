from math import *

def MonPro(a,b,r,nmark,n):
    t=a*b
    m=(t*nmark)%r
    u=(t+m*n)/r
    if(u>=n):
        return (u-n,True)
    else:
        return (u,False)
    
def MonExp(m,d,n):
    dBin=bin(d)
    r = 2**len(dBin)
    nmark = Euclidian(r,n)
    Mbar = (m*r)%n
    Xbar = (1*r)%n
    for i in range(0,len(dBin)):
        Xbar, value = MonPro(Xbar,Xbar,r,nmark,n)
        if(dBin[i] == '1'):
            Xbar, value=MonPro(Mbar,Xbar,r,nmark,n)
    x, value = MonPro(Xbar,1,r,nmark,n)
    print('x',x)
    return x 

def Euclidian(r,n):
    x=r*modinv(r,n)
    y=x-1
    k=y/n
    return k

def bin(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i >>= 1
    return s


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(r, n):
    gcd, x, y = egcd(r, n)
    if gcd != 1:
        return None
    else:
        return x % n

def main():
    MonExp(10,23,29)
    #for i in range(0,100):
        #MonExp(i,x,x)
        

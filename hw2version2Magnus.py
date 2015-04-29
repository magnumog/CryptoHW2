import random
from math import *

def MonPro(a,b):
	t = a*b
	m = (t*nPrime)%r
	u = (t+m*n)/r
	if(u>=n):
		return u-n,True
	else:
		return u,False

def MonExp(M,e,n):
	returnValues = []
	MBar = (M*r)%n
	xBar = (1*r)%n
	for i in range(0,len(e)):
		xBar, value = MonPro(xBar,xBar)
		if e[i]=='1':
			xBar,value = MonPro(MBar,xBar)
		returnValues.append(value)
	x, value = MonPro(xBar,1)
	returnValues.append(value)
	return x,returnValues

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
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def solveRSA():
        returnValues = []
        returnMessage = []
        for i in range(0,100):
                M = random.randint(1000,10000)
                message, value = MonExp(M,bin(d),n)
                returnValues.append(value)
                returnMessage.append(message)

        trueList = []
        falseList = []
        for i in range(0,len(returnValues[0])):
                true=0
                false=0
                for j in range(0,len(returnValues)):
                        if(returnValues[j][i]==True):
                                true = true+1
                        else:
                                false = false+1
                trueList.append(true)
                falseList.append(false)
        number = getNumber(trueList,falseList)
        #print(int(number,2))
        return trueList,falseList,number,int(number,2)

def getNumber(trueList,falseList):
	number = '1'
	for i in range(1,len(trueList)):
		true=trueList[i]
		false=falseList[i]
		if(true>false):
			number = number +'1'
		else:
			number = number + '0'
	return number

def Euclidian(r,n):
    x=r*modinv(r,n)
    y=x-1
    k=y/n
    return k

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
M=10
n=29
d=23
r = 2**(len(bin(d)))
#gcd, rInverse, nPrime = egcd(r,n)
nPrime=Euclidian(r,n)

def main():
	#print(MonExp(10,bin(23),29))
	print(solveRSA())


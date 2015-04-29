
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

def bin(number):
	if number == 0:
        return "0"
    s = ''
    while number:
        if number & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        number >>= 1
    return s

n = 0
#d=wtf
r = 2**(len(bin(n)))
gcd, rInverse, nPrime = egcd(r,n)

def egcd(a,b):
	x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y




import random

def monPro(a,b):
	t = a * b
	m = (t * _n) % r
	u = (t + m * n)/r
	if u >= n:
		return u - n, True
	else:
		return u, False

def monExp(m, e, n):
	result = []
	_m = (m * r) % n
	_c = (1 * r) % n

	for i in e:
		_c, temp = monPro(_c, _c)
		#result.append(temp)
		if i == "1":
			_c,temp = monPro(_m, _c)
		
		result.append(temp)
	c, temp = monPro(_c, 1)
	#result.append(temp)
	result.append(c)
	return result

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def generateSignatures():
	counter = 0

	while counter<100:
		m = random.randint(100,100000)
		#m = 425
		rsa.append(monExp(m, d, n))
		mlist.append(m)
		#print m
		counter += 1

	#for x in range(0, len(rsa)):
		#print rsa[x], mlist[x]

	return rsa, mlist

def solve():
	solved = False
	counter = 0
	st = []
	sf = []
	key = []

	while counter < (len(rsa[0]) - 1):
		tempFail = 0
		tempTrue = 0
		for x in rsa:
			if x[counter] == True:
				tempTrue += 1
			elif x[counter] == False:
				tempFail += 1
		if tempTrue > tempFail:
			print tempTrue, tempFail
			key.append(1)
		elif tempFail >= tempTrue:
			print tempTrue, tempFail
			key.append(0)
		counter += 1
	#print key


rsa = []
mlist = []
#m = 65	
n = 10201
d = str(bin(101))[2:]
r = 2**(len(bin(n))-2)

gcd, _r, _n = egcd(r, n)

if gcd == 1: 
	_n = ((r * _r) - 1) / n
	rsa, mlist = generateSignatures()
	solve()
	#for x in rsa:
		#print x

import random

def monPro(a,b):
	t = a * b
	m = (t * _n) % r
	u = (t + m * n)/r
	#print u , n
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
			#result.append(temp)
		
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
		m = random.randint(100000,100000000)
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


def test ():

	st = []
	sf = []
	temp = []
	# tempFailRSA = 0
	# tempTrueRSA = 0
	# tempFail2 = 0
	# tempTrue2 = 0
	testString = ""
	key = "1"
	while len(key) < (len(bin(n))-1):
		tempFailRSA = 0
		tempTrueRSA = 0
		tempFail2 = 0
		tempTrue2 = 0
		testString = key + "1"
		for x in mlist:
			temp.append(monExp(x, testString, n))
			#print temp
		

		for x in rsa:
			if x[1] == True:
				tempTrueRSA += 1
			elif x[1] == False:
				tempFailRSA += 1
		if tempTrueRSA > tempFailRSA:
			print tempTrueRSA, tempFailRSA
		elif tempFailRSA >= tempTrueRSA:
			print tempTrueRSA, tempFailRSA

		for x in temp:
			if x[-2] == True:
				tempTrue2 += 1
			elif x[-2] == False:
				tempFail2 += 1
		if tempTrue2 > tempFail2:
			print tempTrue2, tempFail2
			key += "1"
		elif tempFail2 >= tempTrue2:
			print tempTrue2, tempFail2
			key += "0"

	print key






rsa = []
mlist = []
m = 65	
n = 3233
d = str(bin(17))[2:]
r = 2**(len(bin(n))-2)
print r

gcd, _r, _n = egcd(r, n)

if gcd == 1: 
	_n = ((r * _r) - 1) / n

	rsa, mlist = generateSignatures()
	#solve()
	test()
	#for x in rsa:
		#print x
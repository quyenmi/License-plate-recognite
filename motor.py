import pickle
import glob
from numpy import mean

global arr,a
arr = []
a = []

def solve(s,t):
	n,m = len(s), len(t)
	i, j = 0, len(s)
	a = []
	t = t.replace("-", "")
	while (i < len(s) -1 and j > 0  ):
		if s[i:] in t:
			cnt1 = s[i:]
			a.append(len(cnt1) / len(t))

		elif s[:j] in t:
			cnt2 = s[:j]
			a.append(len(cnt2) / len(t))
		i += 1
		j -= 1


	i, j = 0, len(s)
	while (i < len(s) - 1 and j > 0):
		if s[i:j] in t:
			cnt = s[i:j]
			a.append(len(cnt) / len(t))

		elif s[i+1:j] in t:
			cnt = s[i+1:j]
			a.append(len(cnt) / len(t))

		elif s[i:j-1] in t:
			cnt = s[i:j-1]
			a.append(len(cnt) / len(t))

		elif s[i+2:j] in t:
			cnt = s[i+2:j]
			a.append(len(cnt) / len(t))

		elif s[i:j-2] in t:
			cnt = s[i:j-2]
			a.append(len(cnt) / len(t))

		elif s[i+3:j] in t:
			cnt = s[i+3:j]
			a.append(len(cnt) / len(t))

		elif s[i:j-3] in t:
			cnt = s[i:j-3]
			a.append(len(cnt) / len(t))
		i += 1
		j -= 1
	m = max(a)
	if m > 0: return m
	else :
		return 0.0

def solve2(s,t):
	n,m = len(s), len(t)
	i, j = 0, len(s)
	t = t.replace("-", "")
	a = []
	test = []
	while (i < len(s) -1 and j > 0  ):
		if s[i:] in t:
			cnt1 = s[i:]
			a.append(len(cnt1) / len(s))
			test.append(cnt1)
		elif s[:j] in t:
			cnt2 = s[:j]
			a.append(len(cnt2) / len(s))
			test.append(cnt2)
		i += 1
		j -= 1


	i, j = 0, len(s)
	while (i < len(s) - 1 and j > 0):
		if s[i:j] in t:
			cnt = s[i:j]
			a.append(len(cnt) / len(s))
			test.append(cnt)

		elif s[i+1:j] in t:
			cnt = s[i+1:j]
			a.append(len(cnt) / len(s))
			test.append(cnt)

		elif s[i:j-1] in t:
			cnt = s[i:j-1]
			a.append(len(cnt) / len(s))
			test.append(cnt)

		elif s[i+2:j] in t:
			cnt = s[i+2:j]
			a.append(len(cnt) / len(s))
			test.append(cnt)

		elif s[i:j-2] in t:
			cnt = s[i:j-2]
			a.append(len(cnt) / len(s))
			test.append(cnt)

		elif s[i+3:j] in t:
			cnt = s[i+3:j]
			a.append(len(cnt) / len(s))
			test.append(cnt)

		elif s[i:j-3] in t:
			cnt = s[i:j-3]
			a.append(len(cnt) / len(s))
			test.append(cnt)

		i += 1
		j -= 1
	# print(test)	
	m = max(a)
	if m > 0: return m
	else :
		return 0.0

def motor(s, t):
	vt = t.find('-')
	cnt, i = 0, 0

	if vt == -1:

		if len(t) > len(s):
			c = solve(s,t)
		else :
			c = solve2(s,t)
	else:
		if len(t) > len(s):
			c = solve(s,t)
		else :
			c = solve2(s,t)

	if vt == -1:
		lm = min(len(s), len(t))
		while (i < lm):
			if (s[i] == t[i]): cnt += 1
			i += 1
	else:
		while (i < len(s) and i < vt):
			if (i < len(s) and s[i] == t[i]): cnt += 1
			i += 1
		i, its = -1, len(s[vt : ])
		while (t[i] != '-' and its > 0):
			if (t[i] == s[i]): cnt += 1
			i -= 1
			its -= 1
	a = cnt / len(s)
	return max(a,c) 	

def cal_motor(test, label):
	# calculate xemay
	with open(test, "rb") as fp:
		test1 = pickle.load(fp)
		fp.close()

	with open(label, "rb") as fp:
		label1 = pickle.load(fp)
		fp.close()

	# print(len(test1))
	# print(len(label1))
	# t = glob.glob(link)
	# print(len(t), len(label1), len(test1))
	xe =[]
	s1 = 0
	for i in range(len(test1)):
		c = motor(label1[i], test1[i])
		s1 +=  c
		if (c == 1.0 and check(label1[i], test1[i])):
			# xe.append(t[i])
			arr.append([i])
		elif c>0.6 and c < 1.0:
			a.append(c)

	avg = (s1, len(label1)) 
	# print('aver of moto = ', str(ave1))
	return avg

def check(s,t):
	vt = t.find('-')

	if vt == -1:
		if len(s) == len(t): return True

		else: return False

	else: 
		if len(t) - 1 == len(s): return True
		else: return False 

def avg_motor():
	xemay = []
	s = 0
	l = 0

	xemay.append(cal_motor("data/motor1.pkl", "data/motor1_xml.pkl"))
	xemay.append(cal_motor("data/motor2.pkl", "data/motor2_xml.pkl"))
	xemay.append(cal_motor("data/motor3.pkl", "data/motor3_xml.pkl"))
	xemay.append(cal_motor("data/motor4.pkl", "data/motor4_xml.pkl"))
	xemay.append(cal_motor("data/motor5.pkl", "data/motor5_xml.pkl"))
	for i in range(len(xemay)):
		s += xemay[i][0]
		l += xemay[i][1]

	return s,l

def getLen1():
	s,l = avg_motor()
	return len(arr), s, l

if __name__ == "__main__":
	n,s,l = getLen1()
	print(n,s,l)
	print(len(arr))
	
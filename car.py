import pickle
import glob
from numpy import mean

global arr, a
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

def car(s, t):
	vt = t.find('-')	
	cnt, i = 0, 0

	if s == 'unk':
		return 1.0

	if vt == -1:
		if len(t) - 1 > len(s):
			c = solve(s,t)
		else :
			c = solve2(s,t)
	else:
		if len(t) - 1 > len(s):
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

def check(s,t):
	vt = t.find('-')

	if vt == -1:
		if len(s) == len(t): return True

		else: return False
	else: 
		if len(t) - 1 == len(s): return True
		else: return False 

def cal(test, label):
	with open(test, "rb") as fp:
		test2 = pickle.load(fp)
		fp.close()

	with open(label, "rb") as fp:
		label2 = pickle.load(fp)
		fp.close()
	s2 = 0
	xe2 = []
	cnt = 0
	for i in range(len(test2)):
		c = car(label2[i], test2[i])
		s2 +=  c
		if (c == 1.0 and check(label2[i], test2[i])):
			arr.append(i)
			
		else: 
			a.append(i)

	avg = (s2, len(label2))
	# print('average of car = ', str(ave2))
	return avg

def avg_car():
	carL = []
	s = 0
	l = 0

	carL.append(cal("data/car1.pkl", "data/car1_xml.pkl"))
	carL.append(cal("data/car2.pkl", "data/car2_xml.pkl"))
	carL.append(cal("data/car3.pkl", "data/car3_xml.pkl"))
	carL.append(cal("data/car4.pkl", "data/car4_xml.pkl"))
	carL.append(cal("data/car5.pkl", "data/car5_xml.pkl"))
	carL.append(cal("data/car6.pkl", "data/car6_xml.pkl"))
	carL.append(cal("data/car7.pkl", "data/car7_xml.pkl"))
	for i in range(len(carL)):
		s += carL[i][0]
		l += carL[i][1]

	

	return s,l

def getLen2():
	s,l = avg_car()
	return len(arr), s, l

if __name__ == "__main__":
	#calculate car
	n,s, l = getLen2()
	print(n,s,l)
	print(len(arr))
from motor import *
from car import *

if __name__ == '__main__':
	a1, b1, c1 = getLen1()
	a2, b2, c2 = getLen2()
	print("Average of car is: ", b1 / c1)
	print("Average of motor is: ", b2 / c2)
	print("Average of both is: ", ((b1 / c1) + (b2 / c2))/2)

	print("total 100% true is: ", (a1 + a2))
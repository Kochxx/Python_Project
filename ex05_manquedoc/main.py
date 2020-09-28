# -*- coding: utf-8 -*-
import sys

# function that prints [start;end[ with a step of a
def printRange(start, end, a):
	x = range(start, end, a)
	res = []
	for n in x:
		res.append(n)
	return res

# main function
if __name__ == '__main__':
    print(printRange(0,15,3))

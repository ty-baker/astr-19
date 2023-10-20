import numpy as np 
import sys

def mypoly(x):
	result = x**3 + 8
	return result

def main():
	i = mypoly(9)
	print(i)
	if i > 27: 
		print("YAY!")

if __name__=="__main__":
	main()
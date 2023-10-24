import numpy as np 

def main():
	x = np.linspace(0, 2*np.pi, 1000)
	y = np.sin(x)
	print(x)
	print(y)

if __name__=="__main__":
	main()
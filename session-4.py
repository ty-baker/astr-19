import sys

class Animal:
# a class for my favorite animal
	def print(self):
		print("My favorite animal is a tarantula.")
		print(f"Length of arms = {self.length_arms}.")
		print(f"Length of legs = {self.length_legs}.")
		print(f"Number of eyes = {self.num_eyes}.")
		if (self.tail==True):
			print ("I have a tail.")
		else:
			print ("I do not have a tail.")

		if (self.furry==True):
			print ("I am furry.")
		else:
			print ("I am not furry.")

	
	def __init__(self, nped, length, numeyes, ntail, nfurry):
		self.length_arms = nped
		self.length_legs = length
		self.num_eyes = numeyes
		self.tail = ntail
		self.furry = nfurry

def main():
	tarantula = Animal(2.0, 8.0, 8, False, True)
	tarantula.print()

if __name__=="__main__":
	main()



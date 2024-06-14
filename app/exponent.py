# Exercise 15: Write a function called exponent(base, exp) that returns 
# an int value of base raises to the power of exp.
from fractions import Fraction

def exponent(base, exp):
	result = base
	for i in range(exp-1):
		result *= base
	return result

def negative_exponent(base, exp):
	inverse_exp = -exp
	return 1/(exponent(base,inverse_exp))

try:
	base = int(input("Please enter your base value: "))
	exp = int(input("Please enter your exponent value: "))
	result = 1
	if(exp >= 0):
		result = exponent(base, exp)
	else: 
		if (exp < 0):
			result = Fraction(negative_exponent(base, exp))
	
	print(base, 'to the power of', exp, 'is:', result)
except ValueError: 
	print("Error. Invalid integer entered. Please try again.")

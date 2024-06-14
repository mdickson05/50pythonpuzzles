# Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is 
# equal to or lower than 1000. Otherwise, return their sum.

def checker(num1, num2):
	if(num_1 * num_2 <= 1000):
		print('The result is', num_1 * num_2)
	else:
		print('The result is', num_1 + num_2)
try:
	num_1 = int(input('Enter your first number: '))
	num_2 = int(input('Enter your second number: '))
	checker(num_1, num_2)
except:
	print('Please enter valid number.')


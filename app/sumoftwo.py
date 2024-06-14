# Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is 
# equal to or lower than 1000. Otherwise, return their sum.

def checker(num1, num2):
	if(num_1 * num_2 <= 1000):
		print('The result is', num_1 * num_2)
	else:
		print('The result is', num_1 + num_2)

print('Enter your first number: ')
num_1 = input()
print('Enter your second number: ')
num_2 = input()

try:
	num_1 = int(num_1)
	num_2 = int(num_2)
except:
	print('Please enter valid integers')

checker(num_1, num_2)

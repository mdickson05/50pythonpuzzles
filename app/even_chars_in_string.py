# Exercise 3: Print characters from a string that are present at an even 
# index number

# Write a program to accept a string from the user and display characters 
# that are present at an even index number.

def construct_even_string(string):
	result = ''
	for i in range(0, len(string)):
		if i % 2 == 0:
			result += string[i]
	return result;

try:
	input = str(input('Please enter a string: '))
	result = construct_even_string(input)
	print('Result:', result)
except:
	print('Please enter a valid string')

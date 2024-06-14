# Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting from zero 
# up to n and return a new string.
import sys

def remove_chars(input, removeTo):
	if len(input) <= removeTo:
		print('Error: index to remove to must be less than the length of your string.')
	else:
		result = input[removeTo:]
		return result;

try:
	input = sys.argv[1]
	removeTo = sys.argv[2]
	pass
except:
	print('''Invalid formatting. Note: format is 
	python remove_n_from_string.py <string Input> <int removeTo>''')
else:
	try:
		removeTo = int(removeTo)
		result = remove_chars(input, removeTo)
		if result != None:
			print(result)
		pass
	except:
		print('Error: please enter a valid integer. ')


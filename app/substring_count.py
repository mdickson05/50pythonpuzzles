# Exercise 7: Return the count of a given substring from a string

# Write a program to find how many times substring “Emma” appears in the 
# given string.

def substring_counter(input_string, string_to_find):
	print('In the string:', input_string)
	result = input_string.count(string_to_find)
	print(string_to_find, 'appeared', result, 'times')

input_1 = "Emma is good developer. Emma is a writer"
input_2 = "Marcus is the best developer"

substring_counter(input_1, "Emma");
substring_counter(input_2, "Emma");


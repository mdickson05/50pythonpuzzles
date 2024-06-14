# Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting from zero
# up to n and return a new string.

def check_if_first_is_last (list):
	first = list[0]
	last = list[len(list) - 1]
	
	if first == last:
		return True
	else:
		return False

def print_outcome(list, result):
	print('List:', list)
	print('Is first and last element equal:', result)


list_1 = [1,4,5,6,1]
result = check_if_first_is_last(list_1);
print_outcome(list_1, result)

list_2 = [7,6,5,7,6]
result = check_if_first_is_last(list_2);
print_outcome(list_2, result)

string_list = ["apple", "banana", "apple"]
result = check_if_first_is_last(string_list);
print_outcome(string_list, result)

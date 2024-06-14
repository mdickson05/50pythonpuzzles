# Exercise 10

# Given two list of numbers, write a program to create a new list such 
# that the new list should contain odd numbers from the first list 
# and even numbers from the second list.

def get_odd_numbers(list):
	result = []
	for i in range(0, len(list)):
		if(list[i] % 2 != 0):
			result.append(list[i])
	return result

def get_even_numbers(list):
	result = []
	for i in range(0, len(list)):
		if(list[i] % 2 == 0):
			result.append(list[i])
	return result

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

odd_list = get_odd_numbers(list1)
even_list = get_even_numbers(list2)

result = odd_list + even_list

print('results list:', result)

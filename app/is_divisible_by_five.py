# Exercise 6: Display numbers divisible by 5 from a list

# Iterate the given list of numbers and print only those numbers which 
# are divisible by 5

def divisible_by_five(list):
	isDivisible = False
	for i in range (0, len(list)):
		if list[i] % 5 == 0:
			if not isDivisible:
				isDivisible = True
				print('Divsible by 5')
			print(list[i])
	return isDivisible

def get_results(list):
	print('Given list is', list)
	result = divisible_by_five(list)

	if not result:
		print('No elements in list are divisible by five')

list = [10,20,33,46,55]
get_results(list)
list = [2,4,3]
get_results(list)

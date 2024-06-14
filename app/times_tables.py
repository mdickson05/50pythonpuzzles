# Exercise 13: Print multiplication table up to given number

def generate_table(limit):
	limit += 1
	for i in range(1, limit):
		result = ''
		for j in range(1, limit):
			result += (str((i * j)) + " ")
		print(result)

try:
	limit = int(input("Please enter your times-table: "))
	generate_table(limit)
except ValueError:
	print("Error. Please enter a valid integer.")

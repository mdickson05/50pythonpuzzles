# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
def pattern(rows):
	for i in range (0, rows):
		num_asterisks = (rows - i)
		asterisks = ""
		for j in range(num_asterisks):
			asterisks += "*"
		print(asterisks)

try:
	rows = int(input("Please enter the number of rows for your pattern: "))
	pattern(rows)
except ValueError:
	print("Error. Please enter valid integer.")

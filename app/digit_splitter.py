# Exercise 11: Write a Program to extract each digit from an integer 
# in the reverse order.

def digit_splitter(num):
	reverse = 0
	split_num = ''
	while(num > 0):
		digit = num % 10
		num = num // 10
		print(digit, end = " ")
	print("")
digit_splitter(1234)


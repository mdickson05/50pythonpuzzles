# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
def reverse_num(number):
	reverse = str(number)[::-1]
	reverse = int(reverse)
	return reverse

try:
	num = int(input('Please enter your number: '))
	reverse = reverse_num(num)
	if(num == reverse):
		print('Yes. Given number is palindrome number')
	else:
		print('No. Given number is not palindrome number.')
except ValueError:
	print('Please enter a valid integer')

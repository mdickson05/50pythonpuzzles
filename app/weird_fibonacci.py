# Exercise 2: Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers, and in each iteration, 
# print the sum of the current and previous number.

prev = 0
for i in range(0, 10):
	result = i + prev
	print('Current number:', i, 'Previous number:', prev, 'Sum:', result)
	prev = i

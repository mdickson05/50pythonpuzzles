def trianglePattern(index):
	for i in range (1, index + 1):
		pattern = ''
		for j in range(0,i):
			pattern += str(i)
		print(pattern)
try:
	length = int(input('Enter the length of your triangle: '))
	pass
except:
	print('Error. Please enter a valid integer')
else:
	if(length > 0 and length < 10):
		trianglePattern(length)
	else:
		print('Error. Number must be between 1 and 9')


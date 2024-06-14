'''
	Need:
	- all products of "range"
	- palindrome in products finder
	- smallest() [palindrome] 
	- largest() [palindrome]
	- factors of palindrome finder
'''

def find_products(start, end):
	products = []
	end += 1
	for i in range(start,end):
		# i = 1
		# i * ? = 1,2,3,4,5,6,7,8,9
		for j in range(i, end):
			product = i * j
			if product not in products:
				products.append(product)
	return products;

def reverse(number):
	reverse = str(number)[::-1]
	reverse = int(reverse)
	return reverse

def find_palindromes(products):
	palindromes = []
	for product in products:
		reversed_num = reverse(product)
		if(product == reversed_num):
			palindromes.append(product)
	return palindromes

def smallest(smallest, min_factor, max_factor):
	factors = []
	for i in range(min_factor, max_factor + 1):
		if smallest % i == 0 and factors.count([int(smallest/i), i]) == 0: 
			if smallest/i > min_factor and smallest/i < max_factor:
				factors.append([i, int(smallest/i)])
	return smallest, factors

def largest(largest, min_factor, max_factor):
	factors = []
	for i in range(min_factor, max_factor + 1):
		if largest % i == 0 and factors.count([int(largest/i), i]) == 0:
			if largest/i > min_factor and largest/i < max_factor:
				factors.append([i, int(largest/i)])
	return largest, factors
			

try: 
	min = int(input("Please enter first value of your range: "))
	max = int(input("Please enter last value of your range: "))

	products = find_products(min, max)
	palindromes = find_palindromes(products)
	palindromes.sort()

	small = palindromes[0]
	smallest_factors = smallest(small, min, max)
	large = palindromes[len(palindromes) - 1]
	largest_factors = largest(large, min, max)

	# print(products)
	# print(palindromes)
	print("Smallest:", smallest_factors)
	print("Largest:", largest_factors)
except ValueError:
	print("Please enter valid integer.")


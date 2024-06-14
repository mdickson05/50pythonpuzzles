# Exercise 12: Tax Calculator
# Rates: 0% for first $10,000; 10% for next $10000, 20% for rest of income
import locale

def calculate_tax(income):
	taxable = income - 10000
	payable = 0

	if(taxable > 0 and taxable <= 10000):
		payable = 0.1 * taxable
	else:
		payable = 0.1 * 10000 + 0.2 * (taxable - 10000)

	return payable

locale.setlocale( locale.LC_ALL, '' )

try:
	income = float(input('Please enter your YTD income: '))
	income_tax = calculate_tax(income)
	if(income_tax > 0):
		print('Income tax payable:', locale.currency(income_tax, grouping=True))
	else:
		print('No tax payable this year!')

except ValueError:
	print('Please enter a valid income.')

*/
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number. For example 220 and 284 are amicable numbers. Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284 Sum of proper divisors of 284 = 1+2+4+71+142 = 220 Write a function to print pairs of amicable numbers in a range.
/*


1.	Code for experiment/practical: Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter Number to Find Factiorial : "))
print(factorial(n))

**************************************************************************************************************************************************

Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number. For example 220 and 284 are amicable numbers. Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284 Sum of proper divisors of 284 = 1+2+4+71+142 = 220 Write a function to print pairs of amicable numbers in a range.

import math
def divSum(n) :	
	result = 0
	for i in range(2, int(math.sqrt(n)) + 1) :
		if (n % i == 0) :
			if (i == int(n / i)) :
				result = result + i
			else :
				result = result+ (i + int(n / i))
	return (result + 1)
def areAmicable(x, y) :
	if (divSum(x) != y) :
		return False
	return (divSum(y) == x)

x = 220
y = 284
if (areAmicable(x, y)) :
	print ("Yes")
else :
	print ("No")

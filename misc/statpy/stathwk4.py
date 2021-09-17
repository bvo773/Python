def number_4():
	print("4) Event- An event is a subset of the sample space. It may consist of one or more outcomes")

def number_5():
	E1 = 0.1
	E2 = 0.1
	E4 = 0.2
	E5 = 0.1

	E3 = 1 - (E1+E2+E4+E5)
	print("5a)", E3)

def number_11():
	legs_only = round(63/108,3)
	wheels_only = round(24/108,3)
	both_legswheels = round(8/108,3)
	neither_legswheels = round(13/108,3)

	print("6)")
	print("legs_only: ", legs_only)
	print("wheels_only: ", wheels_only)
	print("both_legswheels: ", both_legswheels)
	print("neither_legswheels: ", neither_legswheels)

def number_12():
	blue = 25/100
	orange = 21/100
	green = 16/100
	yellow = 14/100
	brown = 13/100
	red = 11/100

	colors = [blue,orange,green,yellow,brown,red]
	colors.sort()
	print("12) colors probabilities: ",colors)

def factorial(n):
	if (n == 0 or n == 1):
		return 1
	else:
		return n * factorial(n-1)

def combination(n, k):
	top = factorial(n)
	x = factorial(k)
	y = factorial(n-k)
	bottom = x * y

	result = top/bottom
	return result

number_4()
number_5()
number_11()
number_12()
print(combination(9,4))

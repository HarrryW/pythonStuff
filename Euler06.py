toBe = 0
sumSquares2 = 0

def squareOfSum():
	i = 0
	for x in range(1,101):
		i += x
		toBe = i **2
	return toBe
	
def sumofSquare():
	sumSquares = 0
	for n in range(1,101):
		sumSquares = sumSquares + n**2
	return sumSquares
	

def main():
	squareOfSum()
	sumofSquare()
	x = squareOfSum()
	y = sumofSquare()
	difference = str(x - y)
	print "Difference = " + difference
main()
def rangeFinder():
	for y in xrange(2520,999999999, 2520):
		if all(y%x==0 for x in range(1,21)):
			return y
		else:
			continue

print rangeFinder()


#Learned to use the all() function (So useful what the hell)
#Learned to use time in the terminal (time python Euler5.py)
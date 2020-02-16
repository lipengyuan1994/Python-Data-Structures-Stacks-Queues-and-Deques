import math

def polysum(n,s):
	area = (0.25*n*s**2)/(math.tan(math.pi/n))
	l = (n*s)**2
	return round((area+l),4) 

print (polysum(4,4))
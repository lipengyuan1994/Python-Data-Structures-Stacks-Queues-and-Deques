def oddTuples(aTup):
	'''
	aTup: a tuple
	
	returns: tuple, every other element of aTup. 
	'''
	count = 1
	out = ()
	for i in aTup:
		if count %2 == 1:
			out = out + (i,)
		count += 1 
		if count > len(aTup):
			break
	
	return out 
	
print (
oddTuples(('I', 'am', 'a', 'test', 'tuple'))
)
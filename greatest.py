liste=[1,3,2,4,5,6,7,9]
def greatest_number(liste):
	s=0
	for n in liste:
		if s<n:
			s=n
	return s
print (greatest_number(liste))
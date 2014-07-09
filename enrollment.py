liste=['UEH',340,3500]
def total_enrollment(liste):
	print("le nombre d'eleve est:")
	s=liste[1]
	print (s)
	print("la recette brute est:")
	d=s*liste[2]
	return d
print (total_enrollment(liste))

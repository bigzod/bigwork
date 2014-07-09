liste=[2,5,7,6,9,8]
def product_list(liste):
	resultat=1
	for n in liste:
		resultat=resultat*n
	return resultat
print (product_list(liste))
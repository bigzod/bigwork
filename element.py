l= [1,3,5,4]
def find_element(liste,n):
    if n in liste:
        s=liste.index(n)
        return s
    else:
        return -1
print(find_element(l,7))

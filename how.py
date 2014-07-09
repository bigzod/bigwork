s=[4,6,9,11]
t=[1,3,5,7,8,10,12]
b=[2]
def how_many_days(a):
	if a in s:
		print(30)
	if a in t:
		print(31)
	if a in b:
		print(28)
print (how_many_days(6))
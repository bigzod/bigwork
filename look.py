index=[]
def add_to_index(index,keyword,url):
	for entry in index:
		if entry[0]==keyword:
			entry[1].append(url)
	index.append([keyword,[url]])
add_to_index(index,"udacity","http://udacity.org")
add_to_index(index,"computing","http://acm.org")
add_to_index(index,"udacity","http://npr.org")
print (index)
















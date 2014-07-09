page=('<a href="http://google.com"/>jggahuwyhrjbhajkdbj<a href="http://facebook.com"/>')
	def get_next_target(page):
	y=page.find('a href')
	d=page.find('"',y)
	c=page.find('"',d+1)
	url=page[d+1:c]
	return url,c
def all_links(page):
	links=[]
	while(True):
		url,end_pos=get_next_target(page)
		if url:
			print (url)
			links.append(url)
			page=page[end_pos:]
		else:
			page=page[end_pos:]
	return links
print (all_links(page))

input=("saisissez votre lien")
def find_input(input,page):
	for a in page:
		if a in input:
			print (a)
		else:
                        break
	return a
print (find_input(input, page))

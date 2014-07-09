page=('<a href="http://udacity.com"><a href="facebook.com"><a href="http://google.com">')
def get_next_target(page):
	n=page.find("a href")
	d=page.find('"', n)
	c=page.find('"', d+1)
	url=page[d+1:c]
	return url,c
def all_links(page):
	while (True):
                url, end_pos=get_next_target(page)
                if url:
                        print (url)
                        page=page[end_pos:]
                else:
                        break
	return url
print (all_links(page))

input=("saisissez votre lien")
def find_links(page):
        for a in input:
                if a in page:
                        y=page.find("a",url)
                        print (y)
                else:
                        break
        return a
print (find_links(page))


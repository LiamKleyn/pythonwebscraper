#This is the one I ended up using

import os
import requests
from lxml import html
import re


for root, directories, filenames in os.walk('/Users/liamkleyn/Desktop/scrapescript/puku2/www.puku.co.za/Books'):
	bookcounter = 0
	for filename in filenames: 
			bookpath = os.path.join(root,filename)
			print bookpath
			bookcounter+=1
			print bookcounter


			page = open(bookpath, 'r')
			content = page.read()
			tree = html.fromstring(content)

			target = open('book.csv', 'a')
			target.write("\n")

			imageUrl = xhtml.xpath('//img[]/@src')
			print imageUrl

			title=tree.xpath('/html/body/div[3]/div[3]/div/div/h2')
			print title[0].text

			author=tree.xpath('/html/body/div[3]/div[3]/div/div/p')
			print author[0].text

			target.write(title[0].text.encode("utf-8"))
			target.write(";")
			target.write(author[0].text.encode("utf-8"))
			target.write(";")

			meta = tree.xpath('//div[contains(@class, "span8")]')
			c = 0
			for elem in meta[0]:
				field = elem.text
				print field
				kids = elem.xpath('//em')
				if (len(kids) <= c):
					kids = elem.xpath('//a')
					target.write(kids[0].text)
				else:
					if kids[c].text:
						field = kids[c].text.encode("utf-8")
						if re.search("\n",field):
							field = re.sub("\n","<br>",field)
						if re.search("\r",field):
							field = re.sub("\r","<br>",field)
						if re.search('\"',field):
							field = re.sub("\"","|",field)
						if re.search('\,',field):
							field = "\"" + field + "\""
						target.write(field)
				target.write(';')
				c+=1
			target.close()


		

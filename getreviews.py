import os
import requests
from lxml import html
import re
from bs4 import BeautifulSoup
import urllib2



bookcounter = 0



for root, directories, filenames in os.walk('/Users/liamkleyn/Desktop/scrapescript/puku2/www.puku.co.za/BookPosts/Details'):
	for filename in filenames: 
			bookpath = os.path.join(root,filename)
			print bookpath
			bookcounter = bookcounter + 1
			print bookcounter


			
			page = BeautifulSoup(open(bookpath),"html.parser")

			
			title= page.find_all('div', {'class' : 'span8'})
			print title

			isbninfo = page.find_all('div', {'class' : 'display-field'})
			print isbninfo
			



			target = open('reviews.txt', 'a')

			target.write("\n")
			target.write("\n")
			target.write(bookpath)
			target.write("\n")
			target.write(str(title))
			target.write("\n")
			target.write("\n")
			target.write(str(isbninfo))

			target.close()

		

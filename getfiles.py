import os
import requests
from lxml import html
import re
bookcounter = 0

for root, directories, filenames in os.walk('/Users/liamkleyn/Desktop/scrapescript/puku2/www.puku.co.za/Books'):
	
	for filename in filenames: 
			bookpath = os.path.join(root,filename)
			print bookpath
			bookcounter = bookcounter + 1
			print bookcounter


			page = open(bookpath, 'r')
			content = page.read()
			tree = html.fromstring(content)



			xpath of review heading
			/html/body/div[3]/div[5]/div/div/div/div/div[2]/div/span

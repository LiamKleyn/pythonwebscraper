import requests
from lxml import html
import re





	
page = open('/Users/liamkleyn/Desktop/scrapescript/puku2/www.puku.co.za/Books/908/Science-Alive-in-the-Home', 'r')
content = page.read()
tree = html.fromstring(content)



title=tree.xpath('/html/body/div[3]/div[4]/div/div/fieldset/div[1]/div[1]/img')
print title[0].text



print "################################"
print "Scraping content from HTML files"
print "################################"

from bs4 import BeautifulSoup
from openpyxl import Workbook
import csv
import urllib2

page = BeautifulSoup(open("/Users/liamkleyn/Desktop/scrapescript/Shaggy.html"),"html.parser")

for authors in page.find_all('div', {'class' : 'default-cover-info'}) :
	print(authors.prettify())

isbninfo = page.find_all('div', {'class' : 'span8'})

isbninfotext = str(isbninfo)
print isbninfotext

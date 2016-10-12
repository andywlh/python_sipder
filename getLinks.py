import re
import urllib2
from bs4 import BeautifulSoup
import socket
import httplib
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getBsObj(url):
	request = urllib2.Request(url)
	request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
	try:
	    html = urllib2.urlopen(request)
	except socket.timeout, e:
	    pass
	except urllib2.URLError,ee:
	    pass
	except httplib.BadStatusLine:
	    pass
	bsObj = BeautifulSoup(html,'html.parser')

	return bsObj

def getExternalLinks(bsObj,excludeUrl):
	externalLinks = []
	for link in bsObj.find_all('a',
						href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def getInternalLinks(bsObj,includeUrl):
	internalLinks = []
	for link in bsObj.find_all('a',href = re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			print link.attrs['href']
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks
def s(filedir):
	urls = []
	urlsR =[]
	files_in = os.listdir(filedir)
	for file in files_in:
		fileUrl = filedir+'/'+file
		f = open(fileUrl,'r')
		for line in f:
			urls.append(line.split('  ')[-1])
	for l in urls:
		if l not in urlsR:
			urlsR.append(l)
	"""f = open(filedir+"/urls.txt",'a')
				for url in urlsR:
					f.write(url+'\n')"""
	return urlsR

def splitUrl(url):
	url_cut = url.replace('http://','').split('/')
	return url_cut

allInLinks = []
def getAllInLinks(url):
	bsObj = getBsObj(url)
	inLinks = getInternalLinks(bsObj,splitUrl(url)[0])
	for link in inLinks:
		if link in allInLinks:
			allInLinks.append(splitUrl(url)[0]+link)
			getAllInLinks(splitUrl(url)[0]+link)

getAllInLinks("http://m.sohu.com")
f = open('./sohu.txt','a')
for link in allInLinks:
	print link+'11111all'
	f.write(link+'\n')


"""num = 0
urls = s("/home/wan/url/url")
for url in urls:
	num = num +1
	HtmlToTxt(url,str(num))"""

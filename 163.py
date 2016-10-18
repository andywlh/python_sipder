#-*-coding:utf-8-*-
import re 
from bs4 import BeautifulSoup
import socket
from getLinks import getBsObj
from getLinks import News
import chardet
import sys
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')
def getCategory(url):
	bsObj = getBsObj(url)
	categorylinks = []
	li = bsObj.find_all('div','subNav')
	for l in li:
		for link in l.find_all('a'):
			categorylinks.append(link['href'])
			#print link['href']
	return categorylinks
def getNewsLinks(url):
	bsObj = getBsObj(url)
	newsLinks = []
	li = bsObj.find_all('div','area areabg1')
	for l in li:
		for link in l.find_all('a'):
			if link['href'] not in newsLinks:
				newsLinks.append(link['href'])
				print (link['href'])
	return newsLinks

def getNew(url):
	bsObj = getBsObj(url)
	body = bsObj.find('div','post_content_main')
	time = body.find('div','post_time_source').get_text().decode('gbk')
	print time.encode('utf-8')
	title = body.find('h1').get_text().decode('gbk')
	#print title
	con = body.find('div','post_body')
	content =''
	for c in con.find_all('p'):
		content += c.get_text().decode('gbk')

	#print  content
	source = url
	new = News(source,title,time,content)
	f = open('./163/1.txt','a')
	f.write(title.encode('utf-8')+'\n'+time+'\n'+source+'\n'+content.encode('utf-8'))

"""categorylinks = getCategory("http://news.163.com/rank")
for cate in categorylinks:
	getNewsLinks(cate)"""

getNew("http://sports.163.com/16/1017/07/C3IIKH270005877U.html")

import re
from bs4 import BeautifulSoup
import urllib2
import sys
import httplib
import socket

reload(sys)
sys.setdefaultencoding('utf-8')

urls = []
request = urllib2.Request("https://123.sogou.com/")
request.add_header('User-Agent',
	'Mozilla/5.0 (Windows NT 6.1; \WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
try:
	html = urllib2.urlopen(request)
except socket.timeout, e:
	pass
except urllib2.URLError, ee:
	pass
except httplib.BadStatusLine:
	pass

soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
	f = open('./hao123.txt','a')
	f.write(str(link.get('href')) + "\n")
	print link.get('href')


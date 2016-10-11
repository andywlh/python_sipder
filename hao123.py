import re
from bs4 import BeautifulSoup
import urllib2
import sys
import httplib
import socket
from html import HtmlToTxt
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
num = 0
for link in soup.find_all('a',href=re.compile("^(http|www).*")):
	num = num + 1
	HtmlToTxt(str(link.get('href')),str(num))
	
	print link.get('href')


import urllib2
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
def HtmlToTxt(url):
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html,'html.parser')
	for s in soup('script'):
		s.clear()
	txt = soup.get_text()
	txt = str(txt)
	txt.replace('\n','')
	txt.replace(' ','')
	txt.replace('\t','')
	f = open('./url.txt','a')
	f.write(txt)

HtmlToTxt('http://toutiao.sogou.com/yule.html')


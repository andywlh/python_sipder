#-*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import socket
import httplib
import sys
import re


global count
count =0 
class Spider(object):
    """Spider"""
    def __init__(self, url):
        self.url = url

    def getNextUrls(self):
        urls = []
        request = urllib2.Request(self.url)
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
        try:
            html = urllib2.urlopen(request)
        except socket.timeout, e:
            pass
        except urllib2.URLError,ee:
            pass
        except httplib.BadStatusLine:
            pass

        soup = BeautifulSoup(html,'html.parser')
        for link in soup.find_all('a'):
            if link.get('href'):
                print("http://m.sohu.com" + link.get('href')+'\n')
                if link.get('href')[0] == '/':
                    urls.append("http://m.sohu.com" + link.get('href'))
                    
                            
        return urls

def getPages(url):
    
    s = Spider(url)
    urls = s.getNextUrls()
    r = urls
    for url in urls:
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
        soup = BeautifulSoup(html,'html.parser')
        for link in soup.find_all('a'):
            if link.get('href') and link.get('href')[0] == '/' :
                print("http://m.sohu.com" + link.get('href')+'\n')
                if ("http://m.sohu.com" + link.get('href')) not in urls:
                    r.append("http://m.sohu.com" + link.get('href'))
    return r                



def saveNews(url):
    global count 
    global html1
    print url
    xinwen = ''
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    try:
        html1 = urllib2.urlopen(request,timeout=10)
    except urllib2.HTTPError, e:
        pass
    except socket.timeout, e:
        pass
    soup = BeautifulSoup(html1,'html.parser')
    for news in soup.select('p.para'):
        xinwen += news.get_text().decode('utf-8')

    if soup.find("h1",{"class":"h1"}):
        title = soup.find("h1",{"class":"h1"}).get_text()
        time = soup.find("div",{"class":"article-info clearfix"}).find(string=re.compile("[0-9].*"))
    else:
        title=''
        time = ''
    
    source = url
    type = ''
    content = xinwen
    n = News(source,title,time,content,type)
    print "2211"
    if n.title:
        count = count +1
        file = open('/home/wan/news/'+str(count)+'.txt','a')
        file.write("标题："+str(n.title)+"   地址："+n.source+"    时间："+str(n.time)+"\n")
        file.write("正文：\n"+n.content)
        file.write("\n")
        file.close()
        print "---------------------------"#-*- coding:utf-8 -*-
    


class News(object):
    """
    source:from where 从哪里爬取的网站
    title:title of news  文章的标题    
    time:published time of news 文章发布时间
    content:content of news 文章内容
    type:type of news    文章类型
    """
    def __init__(self, source, title, time, content, type):
        self.source = source              
        self.title = title                 
        self.time = time                
        self.content = content            
        self.type = type                


reload(sys)
sys.setdefaultencoding('utf-8')

source = "http://m.sohu.com"
urls = Spider(source).getNextUrls()
urls2 =[]
for url in urls:
    print "1111"
    saveNews(url)
    temp = Spider(url).getNextUrls()
    for n in temp:
        if n not in urls2:
            urls2.append(n)
            print "22222"
            saveNews(n)

    



        

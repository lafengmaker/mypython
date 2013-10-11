#encoding:utf8
from bs4 import BeautifulSoup
import urllib2
import time
import random
import os
def openurl(url):
	request = urllib2.Request(url)
	request.add_header('User-Agent', 'Mozilla-Firefox5.0')
	try:
		return urllib2.urlopen(request)
	except:
		print 'error'
	return None
def downloadfile(url,tofolder):	
	print 'imgurl',url
	res=openurl(url)
	if not res:
		print 'error when',url
		return 
	filename=time.strftime('%Y%m%d%H%M%s',time.localtime(time.time()))+str(random.randint(1000,9999))
	ext=url.split('/')[-1];
	if ext.find('.')==-1:
		return ;
	ext=ext.split('.')[1].split('?')[0]
	print ext
	f=open(tofolder+"/"+filename+"."+ext,'w')
	f.write(res.read())
	f.close()
def getSoupLink(uri,tt):
	response=openurl(uri);
	if not response:
		print 'error when',url
		return 
	soup = BeautifulSoup(response)
	return soup.find_all(tt);
def downloadImg(uri,folder):
	print "single page:",uri
	for link in getSoupLink(uri,"img") :
		downloadfile(link.get('src'),folder)
def findaabc(uri):
	for link in getSoupLink(uri,"a") :
		print link.get_text().replace(' ','');
		fol="images/"+time.strftime('%Y%m%d',time.localtime(time.time()))+"/"+link.get_text().replace(' ','')
		if not os.path.exists(fol):
			os.makedirs(fol)
		downloadImg(link.get('href'),fol)
uri="http://book.douban.com/";
findaabc(uri);







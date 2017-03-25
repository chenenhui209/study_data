#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import urllib
import json
import time
item=[]
page=1
while 1:	
	# 获取链接
	url = "https://www.haijinshe.com.cn/invest/investJson.html?type=100&aprSearch=-1&timeSearch=-1&status=-2&style=-2&order=0&searchName=&page=" + str(page)
	print url
	request = urllib2.Request(url=url)
	response = urllib2.urlopen(request)
	result = response.read()
	# item=unicode(item)
	# print item
	# for key in json.loads(item).keys():
	# 	print key
	datalist=json.loads(result)['data']['list']
	# print data
	# 获取表头
	if page==1:
		tag=[]
		for key in datalist[0].keys():
			tag.append(str(key).encode("utf-8"))
		fw=open('AllItem.txt','a')
		for x in xrange(0,len(tag)):
			fw.write(tag[x]+'$')
		fw.close()
		fw=open('AllItem.txt','a')
		fw.write('\n')
		fw.close()
	# datalist=data['list']
	# 如果没有了就停止
	if len(datalist)==0:
		break
	# print type(datalist)
	# 根据表头获取字典中相应的值
	for y in xrange(0,len(datalist)):
		# item.append(datalist[x])
		for a in xrange(0,len(tag)):
			i=str(tag[a])
			attr=[]
			# 如果没有值就显示为0
			if not datalist[y].has_key(i):
				attr.append('0')
			else:
				attr.append(str(datalist[y][i]))
				# 打印出来把握进度
				if i=='name':
					print str(datalist[y][i])
				# 保存ID值
				if i=='id':
					fw=open('AllItemId.txt','a')
					z=str(datalist[y][i]).encode("utf-8")
					fw.write(z+'$')
					fw.close()
			fw=open('AllItem.txt','a')
			for x in xrange(0,len(attr)):
				w=str(attr[x]).encode("utf-8")
				fw.write(w+'$')
			fw.close()
		fw=open('AllItem.txt','a')
		fw.write('\n')
		fw.close()
	page+=1
# print len(item)
# fw=open('AllItem.txt','w')
# for x in xrange(0,len(item)):
# 	w=str(item[x]).encode("utf-8")
# 	fw.write(w+'\n')
# fw.close()


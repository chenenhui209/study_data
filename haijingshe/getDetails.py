#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import urllib
import json
import time


fr=open('AllItemId.txt','r')
for x in fr:
	x=x.strip()
	itemid=x.split('$')
# print itemid
fr.close()
for x in xrange(0,len(itemid)-1):
	id=itemid[x]
	id1=itemid[0]
	page=1
	# id=itemid[0]	
	while 1:	
		# 获取链接
		url = "https://www.haijinshe.com.cn/invest/detailTenderForJson.html?page=" + str(page)+"&id="+str(id)	
		request = urllib2.Request(url=url)
		response = urllib2.urlopen(request)
		result = response.read()
		# item=unicode(item)
		# print item
		# for key in json.loads(item).keys():
		# 	print key
		datalist=json.loads(result)['data']['list']
		# 获取表头
		if (page==1) & (id==id1):
			tag=[]
			fw=open('ItemDetails.txt','a')
			fw.write('itemid'+'$')
			for key in datalist[0].keys():
				tag.append(str(key).encode("utf-8"))
			fw=open('ItemDetails.txt','a')
			for x in xrange(0,len(tag)):
				fw.write(tag[x]+'$')
			fw.close()
			fw=open('ItemDetails.txt','a')
			fw.write('\n')
			fw.close()
		# datalist=data['list']
		# 如果没有了就停止
		if len(datalist)==0:	
			break
		# print type(datalist)
		# 根据表头获取字典中相应的值
		print url
		for y in xrange(0,len(datalist)):
			# item.append(datalist[x])
			fw=open('ItemDetails.txt','a')
			fw.write(str(id)+'$')
			fw.close()
			for a in xrange(0,len(tag)):
				i=str(tag[a])
				attr=[]
				# 如果没有值就显示为0
				if not datalist[y].has_key(i):
					attr.append('0')
				else:
					attr.append(str(datalist[y][i]))
					# 打印出来把握进度
				if i=='id':
					print str(datalist[y][i])
				
				for x in xrange(0,len(attr)):
					fw=open('ItemDetails.txt','a')
					w=str(attr[x]).encode("utf-8")
					fw.write(w+'$')
					fw.close()
			fw=open('ItemDetails.txt','a')
			fw.write('\n')
			fw.close()
		page+=1
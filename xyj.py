import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json

# with open('xyj.txt','r') as fr:
fr=open('xyj.txt','r')
characers=[]
stat={}
for line in fr:
	# line=line.strip()
	# if len(line)==0:
	# 	continue
	# print type(line)	
	print len(line)
	print type(line)
	line=unicode(line)
	print type(line)
	print len(line)
	print(str(line[20])+'&&&&')
	for x in range(0,20):
		print line[x]
	# with open('result1.csv','w') as fw:
	# 	for item in line:
	# 		fw.write(item +'\n')
	# print type(line)
	# for x in xrange(0,len(line)):
		# if not line[x] in characers:
		# 	characers.append(line[x])		
	break
fr.close()
	# 		if not stat.has_key(line[x]):
	# 			stat[line[x]]=0
	# 		stat[line[x]]+=1
	# # print len(characers)
	# # print characers
	# # for key,value in stat.items():
	# # 	print key,value
	# fw=open('result.json','w')
	# fw.write(json.dumps(stat))
	# fw.close
	# stat=sorted(stat.iteritems(),key=lambda d:d[1],reverse=True)
	# # print type(stat),len(stat)
	# for x in xrange(1,20):
	# 	print characers[x]
	# # for x in xrange(1,20):
	# # 	print stat[x][0],stat[x][1]
	# for x in stat:
	# 	print x[0]+','+str(x[1])+'\n'

	# with open('result.csv','w') as fw:
	# 	for item in stat:
	# 		fw.write(item[0]+','+str(item[1]) +'\n')

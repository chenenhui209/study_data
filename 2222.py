import sys
reload(sys)
sys.setdefaultencoding('utf8')

fw = open('data.txt', 'w')
for x in xrange(1 , 10):
	fw.write(str(x)+'\n')
fw.close()
# -*- coding: utf-8 -*- 
import urllib.parse
import urllib.request
from lzStockDebug import debugPrint

# Reference: http://0411.iteye.com/blog/1068239
#
#http://ichart.yahoo.com/table.csv?s=string&a=int&b=int&c=int&d=int&e=int&f=int&g=d&ignore=.csv
#
# s �� ��Ʊ����
# a �� ��ʼʱ�䣬��
# b �� ��ʼʱ�䣬��
# c �� ��ʼʱ�䣬��
# d �� ����ʱ�䣬��
# e �� ����ʱ�䣬��
# f �� ����ʱ�䣬��
# g �� ʱ�����ڡ�
# ?  ����g��ȡֵ��Χ��d->���ա�(day), w->���ܡ�(week)��m->���¡�(mouth)��v->��dividends only��
# ?  �·��Ǵ�0��ʼ�ģ���9�����ݣ���дΪ08��
# Example:
# http://ichart.yahoo.com/table.csv?s=600415.SS&g=d
# # http://ichart.yahoo.com/table.csv?s=600415.SS&a=10&b=8&c=2015&d=0&e=27&f=2016&g=d

stockHistoryUrl = 'http://ichart.yahoo.com/table.csv?s=%s.%s&a=%s&b=%s&c=%s&g=%s'

#Notice: stockCode for Shanghai: ss
#					   ShenZhen: sz
#
def getStockDayData(stockCode, date, flag):
	stockHq = []
	count = 0
	url = stockHistoryUrl%(stockCode[2:], stockCode[:2].upper(), (str)((int)(date[4:6])-1), date[6:], date[:4], flag)
	debugPrint(url)
	try:
		reqAccess = urllib.request.urlopen(url)
	except urllib.error.HTTPError as e:
		print('Warning !!! can not access %s'%url)
		print('Error code:', e.code)
		return stockHq

	stockDayHq = reqAccess.read().decode('gbk','ignore').split('\n')
	for data in stockDayHq:
		try:
			debugPrint(data)
			Date, Open, High, Low, Close, Volumn, Adj = data.split(',')
			if ( Volumn == 'Volume' or Volumn == '000' ):
				pass
			else:
				count += 1
				stockHq.append((Date, Open, High, Low, Close, Volumn, Adj))
		except ValueError:
			pass
	return stockHq
	
if __name__ == '__main__':
	stockHq = getStockDayData('ss600415', '20151118', 'd')
	debugPrint(stockHq)
# -*- coding: utf-8 -*- 
import urllib.parse
import urllib.request

from lzStockDebug import debugPrint

# ���� http://bdcjhq.hexun.com/quote?s2=000001.sh

#the web who provide the stock data 
stockURL = 'http://hq.sinajs.cn/list=s_'
#
verboseStockURL = 'http://hq.sinajs.cn/list='

## -----------------------------------------
##     ����       ��ǰ  �ǵ���  �ǵ�%  ����    �ܶ�
## return: ['�ƴ�Ѷ��','26.67','0.47','1.79','179277','47395']
##------------------------------------------
def getStockHq(stockCode):
	url = stockURL + stockCode
	stockHq = urllib.request.urlopen(url).read().decode('gbk','ignore')
	tmp, stockHq, tmp = stockHq.split('"')
	stockHq = stockHq.split(',')
	debugPrint(stockHq)
	return stockHq

## -----------------------------------------
##            ����     ��  ����  ��ǰ  ���  ���  ��һ  ��һ  ����     �ܶ�      ��һ�� ��һ��                                          ��һ��                                                      ����        ʱ��
## return: [�ƴ�Ѷ��,26.80,26.20,26.67,26.88,25.87,26.66,26.67,17927743,473951677.35,1800,26.66,300,26.65,2900,26.63,8300,26.61,6390,26.60,49600,26.67,34200,26.68,45685,26.69,50800,26.70,9000,26.71,2016-01-22,15:05:49,00]
##------------------------------------------
def getVerboseStockHq(stockCode):
	url = verboseStockURL + stockCode
	stockHq = urllib.request.urlopen(url).read().decode('gbk','ignore')
	tmp, stockHq, tmp = stockHq.split('"')
	stockHq = stockHq.split(',')
	debugPrint(stockHq)
	return stockHq
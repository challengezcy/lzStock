# -*- coding: utf-8 -*- 
from lzStockEnv import monitorStates
from lzStockType import hq,mn,cd
from lzStockHistory import getStockDayData
from lzStockDebug import debugPrint

'''
止损交易系统 (zstd)
规则：-5% 止损
1\ 以持股期间的最高收盘价(zstdHighClose)和买入价(zstdBuyPrice)中的高值(zstdPrice)作为参考;
2\ 当前价(price);
如果满足等式：  (zstdPrice - price)*100/zstdPrice >= 5
则报警提示卖出
'''
zstdPoint = 5
#
#  股票代码    持股期间的最高价(参考上面定义)
zstdData = {}
zstdInit = 0

def zstdInitialize(inHandStock):
	global zstdInit
	if(zstdInit == 0):
		print("zstdInitialize...")
		for stockCode in inHandStock:
			tmpStockCode = stockCode.replace('h','s')
			debugPrint(tmpStockCode, stockCode)
			zstdPrice = inHandStock[stockCode][0]
			stockHq = getStockDayData(tmpStockCode, inHandStock[stockCode][2], 'd')
			print(' 		', 'buyPrice:', zstdPrice)
			for dayData in stockHq :
				print(' 		', dayData[0], dayData[4])
				if ( zstdPrice < dayData[4]):
					zstdPrice = dayData[4]
			zstdData[stockCode] = zstdPrice
			print(' 	', stockCode, zstdData[stockCode])
		zstdInit = 1
	else:
		pass

def zstdFunction(stockCode, monStockHq, inHandStock):
	zstdInitialize(inHandStock)
	debugPrint("zstdFunction processing...")
	zstdPrice = (float)(zstdData[stockCode])
	currentPrice = (float)(monStockHq[hq.price])
	
	debugPrint("zstdFunction: stockCode %s zstdPrice %f, currentPrice %f"%(stockCode, zstdPrice, currentPrice))
	
	if( zstdPrice > currentPrice):
		tmp = ((zstdPrice - currentPrice)/zstdPrice)*100
		if(tmp >= zstdPoint):
			monitorStates[stockCode][mn.price] = currentPrice
			monitorStates[stockCode][mn.state] += 1
			return 1
	else: 
		return 0
		

if __name__ == '__main__':
	zstdInitialize()





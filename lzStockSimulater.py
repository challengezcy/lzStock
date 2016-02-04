# -*- coding: utf-8 -*- 

from lzStockSimulaterEnv import simulaterStock
from lzStockHq import getStockHq
from lzStockType import cd, db
import lzStockOperateDB
import datetime

# sm stands for simulater
def smGetStockFromDb():
	pass
	
def smSaveStockToDb():
	pass

def smInterestStock():
	pass
	
def smBuyStock():
	conn, cu = lzStockOperateDB.initStockDB('.\\simulater.db')
	inhand = lzStockOperateDB.fetchAllItems(conn)
	buyTime = (str(datetime.datetime.now())[:10]).replace('-','')
	index = len(inhand)
	for stock in simulaterStock:
		flag = 0
		for item in inhand:
			if ( item[db.code] == stock and item[db.inhandFlag] == 'T'):
				flag = 1
		if( flag == 1):
			pass
		else :
			index = index + 1
			new = getStockHq(stock)
			newitem = (index, stock, new[cd.name], buyTime, (float)(new[cd.price]), 1000, '', 0, 0, 'T', 'S')
			lzStockOperateDB.insertItem(conn, newitem)
	lzStockOperateDB.closeStockDB(conn, cu)
			
if __name__ == '__main__':
	smBuyStock()
# -*- coding: utf-8 -*- 
from lzStockSimulaterEnv import simulaterStock
from lzStockHumanNotice import humanDailyReport
from lzStockHq import getStockHq
from lzStockType import cd, db
import lzStockOperateDB
import datetime

# sm stands for simulater
''' 
	从数据库中取出所有股票做日常统计
'''
def smStatisticData():
	conn, cu = lzStockOperateDB.initStockDB('.\\simulater.db')
	inhand = lzStockOperateDB.fetchAllItems(conn)
	humanDailyReport(inhand)
	lzStockOperateDB.closeStockDB(conn, cu)
	return

# sm stands for simulater
''' 
	从数据库中取出所有当前持有的股票
'''
def smGetStockFromDb():
	handStock = {}
	conn, cu = lzStockOperateDB.initStockDB('.\\simulater.db')
	curTime = (str(datetime.datetime.now())[:10]).replace('-','')
	inhand = lzStockOperateDB.fetchAllItems(conn)
	for item in inhand:
		if (item[db.inhandFlag] == 'T'): # and curTime != item[db.buyDate]
			handStock[item[db.code]] = [item[db.buyPrice], item[db.buyColumn], item[db.buyDate], item[db.id]]
	lzStockOperateDB.closeStockDB(conn, cu)
	return handStock
	
def smUpdateStockToDb(price, stockDBid):
	conn, cu = lzStockOperateDB.initStockDB('.\\simulater.db')
	sellTime = (str(datetime.datetime.now())[:10]).replace('-','')
	data = (sellTime, price, 1000, 'F', stockDBid)
	lzStockOperateDB.updateItem(conn, data)
	lzStockOperateDB.closeStockDB(conn, cu)
	pass

''' 一键下单购买关注的实验性股票
	1、读取数据库，如果数据库中已有该股票的持有记录，则放弃
	2、若该股票没有持有记录，则买入，同时写入数据库
'''
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
		else:
			new = getStockHq(stock)
			if((float)(new[cd.price]) > 0):
				index = index + 1
				newitem = (index, stock, new[cd.name], buyTime, (float)(new[cd.price]), 1000, '', 0, 0, 'T', 'S')
				print("		 Buy %s %s at price %f"%(stock, new[cd.name], (float)(new[cd.price])))
				lzStockOperateDB.insertItem(conn, newitem)
			else:
				pass
	lzStockOperateDB.closeStockDB(conn, cu)

if __name__ == 'xxxxx':
	smBuyStock()
	handStock = smGetStockFromDb()
	print(len(handStock))

	for stock in handStock:
		smUpdateStockToDb(55.0, handStock[stock][3])
	handStock = smGetStockFromDb()
	print(len(handStock))

	conn, cu = lzStockOperateDB.initStockDB('.\\simulater.db')
	inhand = lzStockOperateDB.fetchAllItems(conn)
	for item in inhand:
		print(item)
	lzStockOperateDB.closeStockDB(conn, cu)

if __name__ == '__main__':
	smStatisticData()
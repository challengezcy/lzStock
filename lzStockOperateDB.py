# -*- coding: utf-8 -*- 
from lzStockDebug import debugPrint
import sqlite3
import os

def connectDB(path):
	if os.path.exists(path):
		print("Connecting to db: %s"%path)
	else: 
		print("Creating and connecting to db: %s"%path)
		
	conn = sqlite3.connect(path)
	return conn
	
def getCursor(conn):
	return conn.cursor()
	
def closeDB(conn, cu):
	try:
		if cu is not None:
			cu.close()
	finally:
		if cu is not None:
			cu.close()
	
def deleteTable(conn, table):
	if table is not None and table != '':
		sql = 'DROP TABLE IF EXISTS ' + table
		debugPrint(sql)
		cu = getCursor(conn)
		cu.execute(sql)
		conn.commit()
	else:
		print("deleteTable Error")
		
def createTable(conn):
	sql = '''create table if not exists `stockList` (
								`id` int(11) NOT NULL,
								`name` varchar(10) NOT NULL,
								`code` varchar(10) NOT NULL,
								`buyTime` varchar(10) NOT NULL,
								`buyPrice` float(10) NOT NULL,
								`buyColumn` int(10) NOT NULL,
								`sellTime` varchar(10),
								`sellPrice` float(10),
								`sellColumn` int(10),
								`inhandFlag` varchar(2) NOT NULL,
								`simuReal` varchar(2) NOT NULL,
								PRIMARY KEY (`id`)
								)'''
	if sql is not None and sql != '':
		cu = getCursor(conn)
		debugPrint(sql)
		cu.execute(sql)
		conn.commit()
	else:
		print("createTable Error")
		
def insertItem(conn, data):
	sql = '''INSERT INTO stockList values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
	if sql is not None and sql != '':
		if data is not None:
			cu = getCursor(conn)
			debugPrint(sql, data)
			cu.execute(sql, data)
			conn.commit()
	else:
		print("insertItem2Table Error")
		
def updateItem(conn, data):
	sql = '''UPDATE stockList SET sellTime = ?, sellPrice = ?,sellColumn = ?,inhandFlag = ? 
											WHERE name = ? and inhandFlag = ? and simuReal = ?'''
	if sql is not None and sql != '':
		if data is not None:
			cu = getCursor(conn)
			debugPrint(sql, data)
			cu.execute(sql, data)
			conn.commit()
	else:
		print("updateItem Error")
		
def deleteItem(conn, sql, data):
	if sql is not None and sql != '':
		if data is not None:
			cu = getCursor(conn)
			debugPrint(sql, data)
			cu.execute(sql, data)
			conn.commit()
	else:
		print("deleteItem Error")
	
def fetchAllItems(conn):
	sql = '''SELECT * FROM stockList'''
	if sql is not None and sql != '':
		debugPrint(sql)
		cu = getCursor(conn)
		cu.execute(sql)
		return cu.fetchall()
	else:
		print("fetchAllItems Error")
		
def initStockDB(path):
	conn = connectDB(path)
	createTable(conn)
	cu = getCursor(conn)
	return conn,cu
	
def closeStockDB(conn, cu):
	closeDB(conn, cu)
	
def getNumRecordsDB(conn):
	record = fetchAllItems(conn)
	return len(record)
	

if __name__ == '__main__':
	conn,cu = initStockDB('.\\test.db')
	data = [(1, '科大讯飞', 'sz002230', '20150202', 25.62, 2000, '', 0, 0, 'T', 'S'),
			(2, '小商品城', 'sh600415', '20150202', 6.03, 2000, '', 0, 0, 'T', 'S'),
			(3, '拓邦股份', 'sz002139', '20150202', 16.10, 2000, '', 0, 0, 'T', 'S'),
			]
	for i in data:
		insertItem(conn, i)
	
	record = fetchAllItems(conn)
	print(len(record))
	for i in record:
		print(i)
	
	i = ('20150203', 6.14, 2000, 'F', '小商品城', 'T', 'S')
	updateItem(conn, i)
	
	sql = '''SELECT * FROM stockList'''
	record = fetchAllItems(conn)
	print(len(record))
	for i in record:
		print(i)
	
	closeStockDB(conn, cu)
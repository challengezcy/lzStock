# -*- coding: utf-8 -*- 
import easygui
from multiprocessing import Process
import datetime
from lzStockType import db

def noticeMessage(noticeStr):
	easygui.msgbox(noticeStr)

def humanNoticeProcess(noticeStr):
	p=Process(target=noticeMessage, args=(noticeStr,))
	p.start()
	
def humanDailyReport(stockInfo):
	curTime = (str(datetime.datetime.now())[:10]).replace('-','')
	inhandStock = []
	buyStock = []
	sellStock = []
	historySell = []
	for item in stockInfo:
		if (item[db.inhandFlag] == 'T'):
			inhandStock.append(item)
		if (item[db.inhandFlag] == 'T' and curTime == item[db.buyDate]):
			buyStock.append(item)
		if (item[db.inhandFlag] == 'F' and curTime == item[db.sellDate]):
			sellStock.append(item)
		if (item[db.inhandFlag] == 'F'):
			historySell.append(item)
	reportFile = "report_"+curTime
	with open(reportFile, "w") as out:
		out.write("------IN HAND------\n")
		out.write("code name			BuyPrice		buyDate\n")
		for i in inhandStock:
			out.write("%s %s		%f		%s\n"%(i[db.code],i[db.name], i[db.buyPrice],i[db.buyDate]))
		out.write("\n")
		out.write("\n")
		out.write("------Today Buy------\n")
		out.write("code name			BuyPrice		buyDate\n")
		for i in buyStock:
			out.write("%s %s		%f		%s\n"%(i[db.code],i[db.name], i[db.buyPrice],i[db.buyDate]))
		out.write("\n")
		out.write("\n")
		out.write("------Today Sell------\n")
		out.write("code name			BuyPrice		buyDate			sellPrice		sellDate\n")
		for i in sellStock:
			out.write("%s %s		%f		%s		%f		%s\n"%(i[db.code],i[db.name], i[db.buyPrice],i[db.buyDate], i[db.sellPrice],i[db.sellDate]))
		out.write("\n")
		out.write("\n")
		out.write("------History Sell------\n")
		out.write("code name			BuyPrice		buyDate			sellPrice		sellDate\n")
		for i in historySell:
			out.write("%s %s		%f		%s		%f		%s\n"%(i[db.code],i[db.name], i[db.buyPrice],i[db.buyDate], i[db.sellPrice],i[db.sellDate]))
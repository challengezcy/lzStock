# -*- coding: utf-8 -*- 
import lzStockSell
from lzStockEnv import candidateStock, monitorStates
from lzStockHq import getVerboseStockHq, getStockHq
from lzStockHumanNotice import humanNoticeProcess
from lzStockType import hq, mn
from lzStockSimulater import smUpdateStockToDb, smGetStockFromDb, smBuyStock

def getCandidateStockHq():
	for stockCode in candidateStock:
		candidateStockHq = getStockHq(stockCode)
		print(candidateStockHq)

def initializeMonitorStructure(handStock):
	print("initializeMonitorStructure ...")
	for stockCode in handStock:
		monitorStates[stockCode] = [0,0,' ']
	lzStockSell.zstdInitialize(handStock)

def monitorInHandStockHq(handStock):
	for stockCode in handStock:
		inHandStockHq = getVerboseStockHq(stockCode)
		noticeFlag = lzStockSell.zstdFunction(stockCode, inHandStockHq)
		if (noticeFlag == 1 and monitorStates[stockCode][mn.state] == 1):
			noticeString = stockCode + ' ' + inHandStockHq[hq.name] + ' ' + inHandStockHq[hq.price]
			humanNoticeProcess(noticeString)
	return
	
def monitorInHandStockHqDB(handStock):
	for stockCode in handStock:
		inHandStockHq = getVerboseStockHq(stockCode)
		noticeFlag = lzStockSell.zstdFunction(stockCode, inHandStockHq)
		if (noticeFlag == 1 and monitorStates[stockCode][mn.state] == 1):
			smUpdateStockToDb(inHandStockHq[hq.price], handStock[stockCode][3])
	return
	
def realInterestStock(handStock):
	monitorInHandStockHq(handStock)
	return

def simulaterInterestStock(handStock):
	monitorInHandStockHqDB(handStock)
	return


if __name__ == '__main__':
	monitorInHandStockHq()
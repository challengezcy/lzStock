# -*- coding: utf-8 -*- 
import lzStockSell
from lzStockEnv import inHandStock, candidateStock, monitorStates
from lzStockHq import getVerboseStockHq, getStockHq
from lzStockHumanNotice import humanNoticeProcess
from lzStockType import hq, mn

monitorStructureInit = 0

def getCandidateStockHq():
	for stockCode in candidateStock:
		candidateStockHq = getStockHq(stockCode)
		print(candidateStockHq)

def initializeMonitorStructure():
	global monitorStructureInit
	if(monitorStructureInit == 0):
		print("initializeMonitorStructure ...")
		for stockCode in inHandStock:
			monitorStates[stockCode] = [0,0,' ']
		monitorStructureInit = 1
	else:
		pass

def monitorInHandStockHq():
	initializeMonitorStructure()
	for stockCode in inHandStock:
		inHandStockHq = getVerboseStockHq(stockCode)
		noticeFlag = lzStockSell.zstdFunction(stockCode, inHandStockHq, inHandStock)
		if (noticeFlag == 1 and monitorStates[stockCode][mn.state] == 1):
			noticeString = stockCode + ' ' + inHandStockHq[hq.name] + ' ' + inHandStockHq[hq.price]
			humanNoticeProcess(noticeString)
	return

def simulaterInterestStock():
	initializeMonitorStructure()
	for stockCode in inHandStock:
		inHandStockHq = getVerboseStockHq(stockCode)
		noticeFlag = lzStockSell.zstdFunction(stockCode, inHandStockHq, inHandStock)
		if (noticeFlag == 1 and monitorStates[stockCode][mn.state] == 1):
			noticeString = stockCode + ' ' + inHandStockHq[hq.name] + ' ' + inHandStockHq[hq.price]
			humanNoticeProcess(noticeString)
	return


if __name__ == '__main__':
	monitorInHandStockHq()
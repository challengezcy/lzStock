# -*- coding: utf-8 -*- 
from multiprocessing import Process, Array, Value
from lzStockSimulater import smUpdateStockToDb, smGetStockFromDb, smBuyStock, smStatisticData
from lzStockEnv import envGetinHandStock, envGetConfig
from lzStockDebug import debugPrint
import sys, os
import time, datetime

import lzStockProcess

processNum = 5

candidateHqPEnable = 1
inHandHqPEnable = 1
simulaterPEnable = 1

# process 1, show the candidate stock Hq
def lzCandidateHq(n,arrflag):
	envGetConfig("lzStock.conf")
	while True:
		if (candidateHqPEnable == 1 and arrflag[1] == 1):
			print('\n''\n ------------------' + 
					time.strftime('%Y-%m-%d : %H-%M-%S', time.localtime(time.time()))
					+ '------------------')
			lzStockProcess.getCandidateStockHq()
			arrflag[1] = 0
		if(arrflag[1] == 2):
			print("trying to reload the candidateStock")
			envGetConfig("lzStock.conf")
			arrflag[1] = 1
		time.sleep(1)


# process 2, monitor the real in hand stock Hq
def lzMonInHandHq(n,arrflag):
	if(inHandHqPEnable == 1):
		while True:
			print("Monitor inHasnd stocks ...")
			envGetConfig("lzStock.conf")
			inHandStock = envGetinHandStock()
			lzStockProcess.initializeMonitorStructure(inHandStock)
			while True:
				if(arrflag[2] == 0):
					lzStockProcess.realInterestStock(inHandStock)
				elif(arrflag[2] == 1 or arrflag[2] == 2):
					arrflag[2] = 0
					break
				time.sleep(1)

#process 3, simulater the in hand stock Hq
def simulater(n,arrflag):
	while True:
		handStock = smGetStockFromDb()
		print("Monitor simulater stocks ...")
		if( len(handStock) == 0 ):
			print("		No simulater stocks, please buy ...")
			time.sleep(120)
		else:
			lzStockProcess.initializeMonitorStructure(handStock)
			while True:
				if(arrflag[3] == 0):
					debugPrint(" 	Start Monitor simulater stocks ...")
					lzStockProcess.simulaterInterestStock(handStock)
					time.sleep(1)
				elif(arrflag[3] == 1):
					arrflag[3] = 0
					break
				elif(arrflag[3] == 2):
					print("		Create daily report ...")
					smStatisticData()
					arrflag[3] = 9
				else:
					time.sleep(120)

#Process 4, create event per the current time
def processNotify(n,arrflag):
	while True:
		ctime = str(datetime.datetime.now())[11:19].replace(':','')
		if( ctime > '092000' and ctime < '092100'):
			arrflag[3] = 1   # 开盘之前,需要重新初始化数据
			arrflag[2] = 1
		elif( ctime > '150300' and ctime < '150400'):
			arrflag[3] = 2   # 收盘之后,生成对应报表
		else: 
			pass
		time.sleep(55)

#Process 5, one key press then buy per the current price
def simBuyStock(n, arrflag):
	while True:
		ctime = str(datetime.datetime.now())[11:19].replace(':','')
		if( not(ctime > '093000' and ctime < '113000' or ctime > '130000' and ctime < '150000') and arrflag[5] == 1):
			print("Not trade time, you can't buy any stock...")
			arrflag[5] = 0
		if(arrflag[5] == 1):
			print("Simulater Buy stock ...")
			smBuyStock()
			arrflag[5] = 0
		time.sleep(1)

def main():
	num = Value('i', 1)
	arrFlag = Array('i', processNum+1)
	p_record = []
	p1 = Process(target=lzCandidateHq, args=(num, arrFlag))
	p2 = Process(target=lzMonInHandHq, args=(num, arrFlag))
	p3 = Process(target=simulater, args=(num, arrFlag))
	p4 = Process(target=processNotify, args=(num, arrFlag))
	p5 = Process(target=simBuyStock, args=(num, arrFlag))
	p_record.append(p1)
	p_record.append(p2)
	p_record.append(p3)
	p_record.append(p4)
	p_record.append(p5)
	for p in p_record:
		p.start()
	
	c = ''
	while(c != 'q'):
		if(c == 'b'):
			print("Tring to buy stock...")
			arrFlag[5] = 1
		if(c == 'h'):
			arrFlag[1] = 1
		if(c == 'u'):
			arrFlag[1] = 2
			arrFlag[2] = 2
		time.sleep(1)
		c = input()
		
	for p in p_record:
		p.terminate()
	for p in p_record:
		p.join()
	
if __name__ == '__main__':
	main()
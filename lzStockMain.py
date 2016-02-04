# -*- coding: utf-8 -*- 
from multiprocessing import Process
import sys, os
import time

import lzStockProcess

def lzCandidateHq():
	time.sleep(60)
	pass
	'''
	while True:
		print('\n''\n ------------------' + 
				time.strftime('%Y-%m-%d : %H-%M-%S', time.localtime(time.time()))
				+ '------------------')
		lzStockProcess.getCandidateStockHq()
		time.sleep(60)
		'''
	
def lzMonInHandHq():
	while True:
		lzStockProcess.monitorInHandStockHq()
		time.sleep(1)
		
def simulater():
	while True:
		time.sleep(8)
		lzStockProcess.simulaterInterestStock()
	
def main():
	p_record = []
	p1 = Process(target=lzCandidateHq)
	p2 = Process(target=lzMonInHandHq)
	p3 = Process(target=simulater)
	p_record.append(p1)
	p_record.append(p2)
	p_record.append(p3)
	for p in p_record:
		p.start()
	
	c = ''
	while(c != 'q'):
		time.sleep(1)
		c = input()
		
	for p in p_record:
		p.terminate()
	for p in p_record:
		p.join()
	
if __name__ == '__main__':
	main()
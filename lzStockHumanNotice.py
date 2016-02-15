# -*- coding: utf-8 -*- 
import easygui
from multiprocessing import Process

def noticeMessage(noticeStr):
	easygui.msgbox(noticeStr)

def humanNoticeProcess(noticeStr):
	p=Process(target=noticeMessage, args=(noticeStr,))
	p.start()
	
def humanDailyReport(stockInfo, flag):
	pass
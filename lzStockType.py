# -*- coding: utf-8 -*- 
from enum import IntEnum

class mn(IntEnum):
	state = 0
	price = 1
	name = 2

class cd(IntEnum):
	name = 0
	price = 1
	difference = 2
	ratio = 3
	column = 4
	amount = 5
	
class db(IntEnum):
	id = 0
	code = 1
	name = 2
	buyDate = 3
	buyPrice = 4
	buyColumn = 5
	sellDate = 6
	sellPrice = 7
	sellColumn = 8
	inhandFlag = 9
	simuReal = 10

class hq(IntEnum):
	name = 0
	open = 1
	close = 2
	price = 3
	high = 4
	low = 5
	buy11p = 6
	sell11p = 7
	column = 8
	amount = 9
	buy1c = 10
	buy1p = 11
	buy2c = 12
	buy2p = 13
	buy3c = 14
	buy3p = 15
	buy4c = 16
	buy4p = 17
	buy5c = 18
	buy5p = 19
	sell1c = 20
	sell1p = 21
	sell2c = 22
	sell2p = 23
	sell3c = 24
	sell3p = 25
	sell4c = 26
	sell4p = 27
	sell5c = 28
	sell5p = 29
	date = 30
	time = 31
	dummy = 32
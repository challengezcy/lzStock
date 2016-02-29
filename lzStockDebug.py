# -*- coding: utf-8 -*- 
lzStockDebug = 0

def debugPrint(*arg):
	if (lzStockDebug == 1 ):
		for var in arg:
			print(var)
	else:
		pass
		

if __name__ == '__main__':
	p = ['a','b','c','d']
	debugPrint(p + p, 'sdfffd')
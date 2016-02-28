# -*- coding: utf-8 -*- 

#the stock I have (dictionary)
#����������class mn(IntEnum)
#   ��Ʊ���� ����� ������ ����ʱ��  
#  'sh600415':[6.83, 1000, 20160120]
inHandStock = {}

# ��Ʊ���� : ����״̬  ��ǰ��        ����
#    xxx   :  [0,       0,            ' ']
monitorStates = {}
		
#the stock pay attention
candidateStock = []

def envGetConfigFromfile(filename):
	tinHandStock = {}
	tcandidateStock = []
	flag = 0
	with open(filename) as source:
		for line in source:
			if(line.strip() == ''):
				continue
			if(line[0] == '@'):
				flag = 1
				continue
			if(line[0] != '#' and flag == 0):
				key, words = line.strip().split(":")
				v1,v2,v3,v4,v5,v6 = words.strip().split(",")
				if((float)(v4) == 0.0):
					tinHandStock[key] = [(float)(v1),(int)(v2),v3.strip()]
			if(line[0] != '#' and flag == 1):
				words = line.strip().split(",")
				if(words[0] == '0'):
					tcandidateStock.append(' ')
				else:
					tcandidateStock.append(words[0])
	return tcandidateStock, tinHandStock
	
def envGetConfig(filename):
	global candidateStock
	global inHandStock
	candidateStock, inHandStock = envGetConfigFromfile(filename)

def envGetinHandStock():
	return inHandStock

def envGetcandidateStock():
	return candidateStock
	
if __name__ == '__main__':
	envGetConfig("lzStock.conf")
	p=envGetcandidateStock()
	print(p)


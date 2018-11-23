#/usr/bin/env python

import csv
import sys
import argparse
from collections import OrderedDict

#Cluster genome
#float, dataframe --> dict, string float
def cluster1(m, file):
	with open(file) as f:
		line=f.readline()
		cluster={}
		while line:
			if line[0]=="@":
				pass
			else:
				i=line.split() #Convert line string to a list
				a=int(i[3]) #Position in float
				b=int(i[0].split('_')[1]) #Reads in float
				c=i[2] #Which chromosome
				if c+'_' + str(a//m) in cluster: #Here cluster by m bp. 
					cluster[c+'_' + str(a//m)]+=b
				else:
					cluster[c+'_' + str(a//m)]=b
			line=f.readline()
		return cluster
		
#Cluster-overlpping 
#float, dataframe --> dict, string float
def cluster2(m,file):
	with open(file) as f:
		line=f.readline()
		cluster={}
		while line:
			if line[0]=="@":
				pass
			else:
				i=line.split()
				a=int(i[3])
				b=int(i[0].split('_')[1])
				c=i[2]
				if c+'_' + str((a+1/2*m)//m) in cluster: #over-lap half m  bp with the fisrt one. 
					cluster[c+'_' + str((a+1/2*m)//m)]+=b
				else:
					cluster[c+'_' + str((a+1/2*m)//m)]=b
			line=f.readline()
		return cluster

#add 0.5 to the key 
#dict-->dict
def cluster3(dict):
	cluster3={}
	for key, val in dict.items():
		s=key.split('_')
		cluster3[s[0] +'_'+ str(int(s[1])+0.5)]=val
	return cluster3
		
#Combine two dicts
#dict, dict --> dict
def combin_dict(x, y):
	z=x.copy()
	z.update(y)
	return z

#save file as csv file
def save_dic(dict):
	w = csv.writer(open("test_output.csv", "w"))
	for key, val in dict.items():
		w.writerow([key, val])
			
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	parser.add_argument('m', type = int,help='first read m')
	args = parser.parse_args()
	result1=cluster1(args.m, args.file)
	result2=cluster2(args.m, args.file)
	result3=cluster3(result2)
	result=combin_dict(result1, result3)
	save_dic(result)

	

if __name__ == '__main__':
	main()

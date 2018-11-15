#/usr/bin/env python

import csv
import sys
import argparse
from collections import OrderedDict

#Cluster genome
def cluster1(file):
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
				if c+'_' + str(a//1000) in cluster: #Here cluster by 1000bp, it can be change to any length. It can be changed to any length.
					cluster[c+'_' + str(a//1000)]+=b
				else:
					cluster[c+'_' + str(a//1000)]=b
			line=f.readline()
		return cluster
		
#Cluster-overlpping 
def cluster2(file):
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
				if c+'_' + str((a+500)//1000) in cluster: #over-lap 500 bp with the fisrt one. If change, over-lapping half of the full length.
					cluster[c+'_' + str((a+500)//1000)]+=b
				else:
					cluster[c+'_' + str((a+500)//1000)]=b
			line=f.readline()
		return cluster
#add 0.5 to the key 
def cluster3(dict):
	cluster3={}
	for key, val in dict.items():
		s=key.split('_')
		cluster3[s[0] +'_'+ str(int(s[1])+0.5)]=val
	return cluster3
		
#Combine two dicts
def combin_dict(x, y):
	z=x.copy()
	z.update(y)
	return z

def save_dic(dict):
	w = csv.writer(open("1_output.csv", "w"))
	for key, val in dict.items():
		w.writerow([key, val])
			
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	args = parser.parse_args()
	result1=cluster1(args.file)
	result2=cluster2(args.file)
	result3=cluster3(result2)
	result=combin_dict(result1, result3)
	save_dic(result)

	

if __name__ == '__main__':
	main()
#/usr/bin/env python

import csv
import sys
import argparse
from collections import OrderedDict
    
def nor_redunt(file):
    
	sRNA_dic={}
	with open(file) as f:
		header=f.readline() 	#read the header line
		seq=f.readline()		#read the sequence line 
		plus=f.readline()		#read the "+" line 
		qual=f.readline()		#read the quality line
		while seq:
			if seq in sRNA_dic:
				sRNA_dic[seq]+=1
			else:
				sRNA_dic[seq]=1
                
			header=f.readline()
			seq=f.readline()
			plus=f.readline()
			qual=f.readline()
            
	return(sRNA_dic)

		#Save for sRNA distribution analysis
def save_dic(dict):
	w = csv.writer(open("output.csv", "w"))
	for key, val in dict.items():
		w.writerow([key.strip(), val])

		#Save for further alignment, can filter the size by len(key.strip() and the reads by the val
def save_dic1(dict):
	with open("1_output3.fasta", "w") as f:
		i=1
		for key, val in dict.items():
			if len(key.strip())<18:
				pass
			elif len(key.strip())>30:
				pass
			else:
				f.writelines('>'+ str(i)+'_'+str(val)+'\n' + key.strip()+'\n')
				i+=1
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	args = parser.parse_args()

	result=nor_redunt(args.file)
	#save_dic(result)
	save_dic1(result)
	

if __name__ == '__main__':
	main()
	
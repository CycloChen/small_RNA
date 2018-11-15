#/usr/bin/evn python

import csv
import sys
import argparse
    
	#Find the length distribution of sRNA in fastq.gz file
def counting(file):
	sRNA_count={}
	with open(file) as f:
		header=f.readline() 	#read the header line
		seq=f.readline()		#read the sequence line 
		plus=f.readline()		#read the "+" line 
		qual=f.readline()		#read the quality line
		while seq:
			seq=seq.strip()
			if len(seq) in sRNA_count:
				sRNA_count[len(seq)]+=1
			else
				sRNA_count[len(seq)]=1
			header=f.readline()
			seq=f.readline()
			plus=f.readline()
			qual=f.readline()
            
	return(sRNA_count)

	
def save_dic(dict):
	w = csv.writer(open("output2.csv", "w"))
	for key, val in dict.items():
		w.writerow([int(key), val])

		
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	args = parser.parse_args()

	result=counting(args.file)
	
	save_dic(result)

if __name__ == '__main__':
	main()
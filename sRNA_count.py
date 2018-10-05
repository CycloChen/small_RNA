
    
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

import csv

def save_dic(dict):
	w = csv.writer(open("output.csv", "w"))
	for key, val in sRNA_dic.items():
		w.writerow([key, val])
	

import sys
import argparse
		
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	args = parser.parse_args()

	return(nor_redunt(args.file))
	

if __name__ == '__main__':
	main()
	
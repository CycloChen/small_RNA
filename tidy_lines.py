#/usr/bin/evn python

import csv
import sys
import argparse

#Filter the alignment lines from .sam file
#.sam to .sam file
#list --> list
def tidy_lines(file):
	with open(file) as f:
		line=f.readline()
		l=[]
		while line:
			if line[0]=="@":
				l.append(line) #keep all the informaition from original .sam file
			else:
				if (int(line.split()[1])==0 or 
				int(line.split()[1])==16
				):
					l.append(line)
				else:
					pass
			line=f.readline()
		return l
		
def save_list(list):
	with open('test_1.sam', 'w') as f:
		for i in list:
			f.write(i)
			
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	args = parser.parse_args()
	result=tidy_lines(args.file)
	save_list(result)
	

if __name__ == '__main__':
	main()
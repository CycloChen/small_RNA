#/usr/bin/env python

import csv
import sys
import argparse


def filter_Chr(file):
    with open(file) as f:
        line=f.readline()
        Chr1D=[]
        while line:
            if line[0]=="@":
                pass            
            elif line.split()[2]=="chr1D":
                Chr1D.append(line)
            else:
                pass
            line=f.readline()
            
        return Chr1D

		
def save_list(list):
	with open('output.txt', 'w') as f:
		for i in list:
			f.write(i + '\n')
			
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	args = parser.parse_args()

	result=filter_Chr(args.file)

	save_list(result)
	

if __name__ == '__main__':
	main()
	
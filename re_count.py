#/usr/bin/evn python

import sys
import argparse
    
def re_count(file):
    with open(file) as f:
        count=0
        line1=f.readline()
        line2=f.readline()
        while line1.startswith('>'):
            l=line1.split('_')
            count=count +int(l[1])
            
            line1=f.readline()
            line2=f.readline()
        print(count)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='first read file')
	args = parser.parse_args()
	re_count(args.file)

	
	

if __name__ == '__main__':
	main()
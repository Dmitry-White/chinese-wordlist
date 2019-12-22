'''
Alex Michael

Todo:
- [ ] Get file length, print progress
'''
import os
import sys
import time

import argparse

from googletrans import Translator
from tqdm import tqdm

def translate(word):
	return Translator().translate(word,src='zh-cn',dest='en').text

def pronounce(word):
	return Translator().translate(word,src='zh-cn',dest='zh-cn').pronunciation

def print_chinese(output):
	output = output.encode('utf8') + os.linesep.encode('utf8')
	sys.stdout.buffer.write(output)

def check_file_valid(fname):
	return os.path.exists(fname)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('infile',help='name of wordlist input file')
	parser.add_argument('-o','--output', help='name of output file')
	parser.add_argument('-t','--tag',type=str, help='add a tag to the file')

	args = parser.parse_args()
	outfile = None if args.output is None else args.output[0]
	tag = None if args.tag is None else args.tag
	infile = args.infile

	# clean tag if provided
	if tag is not None:
		tag = ',,'+tag.replace(',','')

	if outfile is None:
		outfile = infile.split('/')[-1].split('.')
		if len(outfile) > 0:
			outfile[-1] = 'csv'
			outfile ='.'.join(outfile)
		else:
			outfile = '.'.join([outfile,'csv'])


	print(f'Input file:\t{infile}')
	print(f'Output file:\t{outfile}')

	# add all words to an array
	words = []
	with open(infile, encoding='utf8') as f:
		word = f.readline().strip()[1:]
		while word:
			words.append(word)
			word = f.readline().strip()

	# write all words to a file
	with open(outfile, 'w', encoding='utf8') as f:
		for word in tqdm(words):
			translation = 'translation'#translate(word)
			pronunciation = 'pronounciation'#pronounce(word)	

			row = word+','+pronunciation+','+translation
			if tag is not None:
				row += tag
			row+=os.linesep
			f.write(row)
		

if __name__ == '__main__':
	main()


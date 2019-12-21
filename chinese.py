
import os
import sys

from googletrans import Translator

def translate(word):
	return Translator().translate(word,src='zh-cn',dest='en').text

def pronounce(word):
	return Translator().translate(word,src='zh-cn',dest='zh-cn').pronunciation

def print_chinese(output):
	output = output.encode('utf8') + os.linesep.encode('utf8')
	sys.stdout.buffer.write(output)

def main():
	fname = sys.argv[1]
	with open(fname, encoding='utf8') as f:
		word = f.readline().strip()[1:]
		while word:
			translation = translate(word)
			pronunciation = pronounce(word)	

			print_chinese(word+','+pronunciation+','+translation)

			# iterate
			word = f.readline().strip()


if __name__ == '__main__':
	main()


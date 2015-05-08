#  Split single fasta file with multiple entries into multiple files with single entries
#  sys.argv[1] is the input fasta file

import sys
import os

maindir = os.getcwd()

#os.mkdir('./results')
resultsdir = './results'

#  Counts the number of > that appear in the inputted fasta file
def count_entries(fasta_input):
	with open(fasta_input, 'r') as fasta_file:
		fasta_string = fasta_file.read()
	return fasta_string.count('>')
	
#  Creates a list of filenames
def namelist(fasta_input):
	fylenames=[]
	with open(fasta_input, 'r') as fasta_file:
		for line in fasta_file:
			if line.startswith('>'):
				splitline = line.split('_')
				fylenames.append(splitline[0])
	return fylenames

foo = namelist(sys.argv[1])

#  Creates the files
def file_writer(fasta_input):
	with open(fasta_input, 'r') as boo
	os.chdir('./results')
	for i in foo:
		
		

if __name__ == '__main__':
	count_entries(sys.argv[1])
	namelist(sys.argv[1])
	file_writer(sys.argv[1],entries)
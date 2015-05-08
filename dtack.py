#David Tack for Vivienne Lam 3/1/2013
#If file are MAC formatted, let me know!
#If the command line isnt working for you, also, let me know.
import sys
import os

def fasta_splitter(fasta_file,out_dir):
  '''Spits the file by Sequence'''
  with open(fasta_file,'r') as f:
    newdyr = './'+out_dir
    os.mkdir(newdyr)
    os.chdir(newdyr)
    fp = open('header','w')
    for line in f:
      if line.startswith('>'):
	fp = open(line.split()[0][1:],'w')
      fp.write(line)

if __name__ == '__main__':
  print ''  
  fasta_splitter(sys.argv[1],sys.argv[2])
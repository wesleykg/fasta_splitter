import sys, os, re

def splitter(input):
    with open(input, "r") as file:
        if os.path.isdir(outdir) == False:
            os.mkdir(outdir)
        os.chdir(outdir)
        for i in file:
            print i

outdir = "genes.fa"
outdir = "genes" + "_out"

if __name__ == '__main__':
    splitter("genes.fa")

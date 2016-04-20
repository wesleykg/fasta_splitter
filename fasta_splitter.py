'''Usage: fasta_splitter.py <fasta_file>'''

from Bio import SeqIO

from docopt import docopt # For command-line arguments
cmdln_args = docopt(__doc__) # Creates a dictionary of command-line arguments
in_fasta = cmdln_args.get('<fasta_file>')

for record in list(SeqIO.parse(in_fasta, 'fasta')):
    filename = record.id + '.fasta'
    with open(filename, 'w') as out_fasta:
        SeqIO.write(record, out_fasta, 'fasta')
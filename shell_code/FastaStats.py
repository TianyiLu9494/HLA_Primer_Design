from argparse import ArgumentParser
from Bio import SeqIO

class FastaStats(object):
    def __init__(self):
        self.seq_list = []
        self.seq_dict = {}
        
    def parser_arg():
        description = "Read one or more FASTA files, store all sequences in disctionary and a list of sequence ID in original order."
        parser = ArgumentParser( description = description )
        parser.add_argument('fasta_file',
                            metavar = 'FASTA_FILE',
                            type = str,
                            help = 'Input FASTA files')
        return parser.parse_args()
    
    def store_seq(self, fasta_file):
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            file_list.append(seq_record.id)
            file_dict[seq_record.id] = seq_record.seq
def main():
    options = FastaStats().parser_arg()
    FastaStats.store_seq(options.fasta_file)
    print(seq_list)
if __name__ == '__main__':
    main()
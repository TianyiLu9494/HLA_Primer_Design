import argparse

def Main():
    description = "Read one or more FASTA files, store all sequences"\
    +"in disctionary and a list of sequence ID in original order."
    parser = argparse.ArgumentParser( description = description )
    parser.add_argument('fasta_file',
    					nargs = "*",
                        metavar = 'FASTA_FILE',
                        type = str,
                        help = 'Input FASTA files')
    return print(parser.parse_args())

if __name__ == '__main__':
	Main()
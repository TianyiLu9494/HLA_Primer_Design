from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat import MatrixInfo as matlist


matrix = matlist.blosum30

file = sys.argv[1]
exon_file = sys.argv[2]

with open(file.replace('.fasta','_exon2.fasta'),"w") as output_handle:
	W = {}
	seq1 = SeqIO.read(exon_file,"fasta")
	for seq_record in SeqIO.parse(file,"fasta"):
	    align = pairwise2.align.localds(seq1.seq,seq_record.seq, matrix, -10, -0.5)
	    if len(align) == 1: #if there is only one alignment
	        start = align[0][3]
	        end = align[0][4]
	        sliced_seq = seq_record[start:end]
	        SeqIO.write(sliced_seq, output_handle, "fasta")
	    else:
	        W[seq_record.id] = (len(align))

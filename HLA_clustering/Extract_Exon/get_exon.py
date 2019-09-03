import sys
from Bio import SeqIO
from Bio.SubsMat import MatrixInfo as Matlist
from Bio import pairwise2

matrix = Matlist.blosum30
name = sys.argv[1]
exon = SeqIO.read(open(sys.argv[2]))
count = 0
cnt = 0

with open(name.replace(".fasta", "_exon.fasta"), "w") as handle:
    for rec in SeqIO.parse(open(name), "fasta"):
        count += 1
        align = pairwise2.align.localds(exon.seq, rec.seq, matrix, -10, -0.5)
        if len(align) == 1:
            cnt += 1
            start = align[0][3]
            end = align[0][4]
            sliced_seq = rec[start:end]
            rec.description.replace(rec.description[-7::], str(len(rec.seq))+" bp")
            # Add this record to list
            SeqIO.write(rec, handle, "fasta")
        print('  Reads processed  ', count,  ' \r')

print(cnt, "extracted exon reads saved")
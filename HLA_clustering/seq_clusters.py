from Bio import SeqIO
import os
clstr = read_clstr("A_EX2_c0.95.fasta.clstr")
out_dic = {}

with open("../A_exon2_nr.fasta","r") as f:
    for rec in SeqIO.parse(f,"fasta"):
        rec_name =  rec.name[-8:]
        for key in clstr.keys():
            out_dic[key] = []
            if rec_name in clstr[key]:
                out_dic[key].append(rec)
print(out_dic.keys())
from Bio import SeqIO
clstr = read_clstr("A_EX2_c0.95.fasta.clstr")
out_dic = {}
count = 0
rc = 0
with open("../A_exon2_nr.fasta","r") as f:
    for key in clstr.keys():
        out_dic[key] = []
    for rec in SeqIO.parse(f,"fasta"):
        rc += 1
        rec_name =  rec.name[-8:]
        for key in clstr.keys():
            if rec_name in clstr[key]:
                out_dic[key].append(rec)
                count += 1
print(rc)
print(count)
for key in out_dic.keys():
    out_file_name = "../A_exon2_nr.fasta".replace("nr.fasta", key+".fasta")
    with open(out_file_name,"w") as outfile:
        SeqIO.write(out_dic[key], outfile, "fasta")
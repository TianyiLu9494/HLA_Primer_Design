import os
os.chdir("../Data/Sequences/cd-hit/")

def run_cdhit(inf):
    threshold = input("Enter the threshold: ")
    outf = inf.replace(".fasta","_c{}.fasta".format(threshold))
    cdhit_cmd = "cd-hit -i {} -o ./cd-hit/{} -c {}".format(inf, outf, threshold)
    os.system(cdhit_cmd)

def read_clstr(inf):
    with open(inf,"r") as f:
        clstr = dict()
        for line in f:
            if line[0] is ">":
                a = line[1:8]
                b = line[9:10] # when using split() there is a /n automatically generated
                ls_name = a+b
                clstr[ls_name] = []
            else:
                id = line.split(" ")[1][5:13]
                clstr[ls_name].append(id)
    cls_nb = len(clstr.keys())
    print("{} clusters has been read.".format(cls_nb))
    return clstr


from Bio import SeqIO
import os
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


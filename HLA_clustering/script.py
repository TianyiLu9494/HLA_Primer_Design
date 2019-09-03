import os
from my_pipeline import cdhit as cd

os.chdir("../Data/Sequences/")
#outpath = cd.kill_rd("A_exon2.fasta")
outpath = cd.cluster("A_exon2_nr.fasta")
clstr = cd.read_clstr(outpath)
cd.write_clstr(clstr)
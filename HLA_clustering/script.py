import os
from my_pipeline import cdhit as cd

os.chdir("../Data/Sequences/")
cd.kill_rd("A_exon2.fasta")
cd.cluster()
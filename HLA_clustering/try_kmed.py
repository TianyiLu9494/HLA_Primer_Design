from my_pipeline.kmed import kmed_grouping as kg
import os
os.chdir("../Data/Alignments/")
kgins = kg("clustalw_A_exon2.aln")
kgins.get_subaln(3)
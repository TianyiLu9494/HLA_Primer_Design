
infile = sys.agrv[1]

#clustalw
def cmd_clustalW():
	clustalw_exe = "/Users/tianyilu/Tools/MSA/clustalw-2.1-macosx/clustalw2"
	outfile = infile.replace('.fasta','_clustalw.aln')
	my_clustal_cmd = clustalw_exe + " -INFILE=" + infile +  " -OUTFILE=" +outfile
	os.system(my_clustal_cmd)

def mafft():
	from Bio.Align.Applications import MafftCommandline
	from io import StringIO
	from Bio import AlignIO
	mafft_cline = MafftCommandline("mafft", input=infile)
	print(mafft_cline)
	stdout,stderr = mafft_cline()
	align = AlignIO.read(StringIO(stdout), "fasta")
	outfile = infile.replace('.fasta','_mafft.aln')
	AlignIO.write(align,outfile,"clustal")


def ProbCons():
	from Bio.Align.Applications import ProbconsCommandline
	pbcn_exe = "/Users/tianyilu/Tools/MSA/probcons/probcons"
	probcons_cline = ProbconsCommandline(pbcn_exe,infile,clustalw=True)
	print(probcons_cline)
	stdout, stderr = probcons_cline()
	with open(infile.replace('.fasta','_probcons.aln'), "w") as handle:
    	handle.write(stdout) 
#!/usr/bin/env python3.6

from Bio import SeqIO
import os
import math
import sys

def _fastq_convert_fasta(in_handle, out_handle, alphabet=None):
        """Fast FASTQ to FASTA conversion (PRIVATE). 
        Avoids dealing with the FASTQ quality encoding, and creating SeqRecord and 
        Seq objects in order to speed up this conversion. 
        NOTE - This does NOT check the characters used in the FASTQ quality string 
        are valid! 
        """

        from Bio.SeqIO.QualityIO import FastqGeneralIterator
        # For real speed, don't even make SeqRecord and Seq objects! 
        count = 0
        for title, seq, qual in FastqGeneralIterator(in_handle):
                count += 1
                out_handle.write(">%s\n" % title)
        # Do line wrapping 
                for i in range(0, len(seq), 60):
                        out_handle.write(seq[i:i + 60] + "\n")
        return count

name = sys.argv[1]
min =float(input('enter minimum length: '))
max =float(input('enter maximum length: '))
qs = float(input('Enter quality score: '))

qual_sequences = [] # Setup an empty list
cnt = 0
count= 0
  
with open(name.replace('.fastq', '_filtered.fasta'), 'w') as output_handle:
        for rec in SeqIO.parse(open(name), "fastq") :
                count += 1
                rec.letter_annotations["phred_quality"]
                probs = []
                for q in rec.letter_annotations["phred_quality"]:
                        e = float(math.pow(10.0,-1*(float(q)/10.0)))
                        probs.append(e)
                av_prob = float(sum(probs))/float(len((rec.letter_annotations["phred_quality"])))
                av_q = float(-10.0*(math.log10(float(av_prob))))
                if len(rec.seq) >=min and len(rec.seq) <=max and av_q >= qs:
                        cnt += 1
                        # Add this record to our list
                        SeqIO.write(rec, output_handle, "fasta")
                print('  Reads processed  ', count ,  ' \r')

os.system("sed -i -n '1~4s/^@/>/p;2~4p' " + name.replace('.fastq', '_filtered.fasta'))
print(cnt,'filtered reads saved')

def screening_IC(aln):
    from Bio.Align import AlignInfo
    from Bio.Alphabet import IUPAC
    from Bio.SubsMat import FreqTable
    summary_align = AlignInfo.SummaryInfo(aln)
    g_consensus = summary_align.gap_consensus()
    expect_freq = {'A' : .3, 'G' : .2, 'T' : .3, 'C' : .2}
    e_freq_table = FreqTable.FreqTable(expect_freq, FreqTable.FREQ,
                                       IUPAC.unambiguous_dna)
    info_arr = []
    for i in range(len(g_consensus)):
        j = i + 25
        if(j<len(g_consensus)):
            info_content = summary_align.information_content(i,j,
                                                         e_freq_table = e_freq_table,
                                                         chars_to_ignore = ['X'])
        else:
            info_content = summary_align.information_content(i,len(g_consensus),
                                                         e_freq_table = e_freq_table,
                                                         chars_to_ignore = ['X'])

        # print(info_content)
        info_arr.append(info_content)
    def plot():
        import numpy as np
        import matplotlib.mlab as mlab
        import matplotlib.pyplot as plt

        num_bins = 10

        # histogram
        # n, bins, patches = plt.hist(info_arr, num_bins, facecolor='blue', alpha=0.5)

        plt.scatter(range(len(g_consensus)), info_arr, )
        plt.show()

    return plot

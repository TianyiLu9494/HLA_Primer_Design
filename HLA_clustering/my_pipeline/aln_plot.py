class Screening():
    def __init__(self, file):
        from Bio import AlignIO
        self.alignment = AlignIO.read(file, "clustal")

    def __per_iden(self):
        from Bio.Align import AlignInfo
        summary_align = AlignInfo.SummaryInfo(self.alignment)
        consensus = summary_align.gap_consensus()
        my_pssm = summary_align.pos_specific_score_matrix(consensus)
        ts = len(self.alignment)
        Iden = []
        consensus = list(consensus)
        for i in range(0, len(consensus)):  # how to deal with "X"
            if consensus[i] == "X":
                nude = max([(value, key) for key, value in my_pssm[i].items()])
                consensus[i] = nude[1]  # replace the X
                Iden.append(nude[0] / ts)
            else:
                score = max(my_pssm[i].values()) / ts
                Iden.append(score)
        return Iden

    def avgw_plt(self, k=1):
        from statistics import mean
        avg_i = []
        iden = self.__per_iden()
        for i in range(0, len(iden) - k + 1):
            score = mean(iden[i:i + k])
            avg_i.append(score)
        import matplotlib.pyplot as plt
        plt.scatter(range(len(avg_i)), avg_i)
        plt.xlabel('position')
        plt.ylabel('average percentage identity of {}bp window'.format(k))
        plt.show()

    def win_cout(self, k=15):
        import seaborn as sns
        import matplotlib.pyplot as plt
        ws = []
        iden = self.__per_iden()
        for i in range(0, len(iden) - k + 1):
            count = 0
            for i in iden[i:i + k]:
                if i == 1:
                    count += 1
            ws.append(count)
        sns.countplot(x=ws)
        plt.show

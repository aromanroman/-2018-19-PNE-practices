from Seq import Seq
seq1 = Seq("ACTCTGAGTTT")
seq2 = Seq("AGTCAACTAAC")
seq3 = Seq(seq1.complement())
seq4 = Seq(seq3.reverse())

print("Sequence 1:{}".format(seq1.strbase))
print("   Length: {} ".format(seq1.len()))
print("   Bases count: A: {}, T:{}, C: {}.G: {}".format(seq1.count("A"), seq1.count("T"), seq1.count("C"), seq1.count("G")))
print("   Bases percentage:A:{}, T:{}, C:{}, G:{}".format(seq1.perc("A"), seq1.perc("T"), seq1.perc("C"), seq1.perc("G")))

print("Sequence 2:{}".format(seq2.strbase))
print("   Length: {} ".format(seq2.len()))
print("   Bases count: A: {}, T:{}, C: {}.G: {}".format(seq2.count("A"), seq2.count("T"), seq2.count("C"), seq2.count("G")))
print("   Bases percentage:A:{}, T:{}, C:{}, G:{}".format(seq2.perc("A"), seq2.perc("T"), seq2.perc("C"), seq2.perc("G")))

print("Sequence 3:{}".format(seq3.strbase))
print("   Length: {} ".format(seq3.len()))
print("   Bases count: A: {}, T:{}, C: {}.G: {}".format(seq3.count("A"), seq3.count("T"), seq3.count("C"), seq3.count("G")))
print("   Bases percentage:A:{}, T:{}, C:{}, G:{}".format(seq3.perc("A"), seq3.perc("T"), seq3.perc("C"), seq3.perc("G")))

print("Sequence 4:{}".format(seq4.strbase))
print("   Length: {} ".format(seq4.len()))
print("   Bases count: A: {}, T:{}, C: {}.G: {}".format(seq4.count("A"), seq4.count("T"), seq4.count("C"), seq4.count("G")))
print("   Bases percentage:A:{}, T:{}, C:{}, G:{}".format(seq4.perc("A"), seq4.perc("T"), seq4.perc("C"), seq4.perc("G")))
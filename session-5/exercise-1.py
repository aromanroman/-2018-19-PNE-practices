def count_a(seq):
    """this will be used for counting the number of a's"""

    result = 0
    for b in seq:
        if b == 'A':
            result += 1

    return result
def count_c(seq):
    """this will be used for counting the number of a's"""

    result = 0
    for b in seq:
        if b == 'C':
            result += 1

    return result
def count_g(seq):
    """this will be used for counting the number of a's"""

    result = 0
    for b in seq:
        if b == 'G':
            result += 1

    return result
def count_t(seq):
    """this will be used for counting the number of a's"""

    result = 0
    for b in seq:
        if b == 'T':
            result += 1

    return result


s =input("Enter the sequence: ")
tl = len(s)
print("This sequence is {} bases in length".format(tl))


def count_bases(seq):
	na = count_a(seq)
	ng = count_g(seq)
	nc = count_c(seq)
	nt = count_t(seq)

	counter_bases_dic = {"A": na,"C":nc,"T":nt,"G":ng}

	pa=(round(100.0 * na / tl, 1))
	pt=(round(100.0 * nt / tl, 1))
	pc=(round(100.0 * nc / tl, 1))
	pg=(round(100.0 * ng / tl, 1))
	for k in counter_bases_dic:
		print("Base ", k)
		print("Counter:", counter_bases_dic[k])
		if k=="A":
			print("Porcentage: ", na)
		elif k=="C":
			print("Porcentage: ", nc)
		elif k=="G":
			print("Porcentage: ", ng)
		elif k=="T":
			print("Porcentage: ", nt)






count_bases(s)





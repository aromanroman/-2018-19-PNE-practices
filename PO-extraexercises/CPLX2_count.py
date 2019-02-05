with open("CPLX2.txt","r") as f:

    counter_a = 0
    counter_c =0
    counter_t = 0
    counter_g = 0
    for line in f:
        if line[0]==">":

            continue

        counter_a += line.count("A")
        counter_c += line.count("C")
        counter_t += line.count("T")
        counter_g += line.count("G")


    print("the counter of A is: ",counter_a)
    print("the counter of T is: ", counter_t)
    print("the counter of G is: ", counter_g)
    print("the counter of C is: ", counter_c)






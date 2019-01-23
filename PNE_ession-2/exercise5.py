def countbases(file_name):
    elements=[]
    with open(file_name,"r") as f:
        for line in f:
            line.replace("\n","").split(",")
            elements.append(line)
    n=0
    counter=0
    while n<len(elements):
        for n in range(len(elements)):
            counter1=elements[n].count()
            counter+=counter1
        n+=1

    print("the total lenght of the sequence in the file is:",counter)
    print("the elements are: ", elements)

selection=input("select the name of the file that you want to choose: ")
countbases(selection)
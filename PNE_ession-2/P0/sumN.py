number=int(input("select the number with which you want to use to perfom the sum of the number first integer:  "))
def sum(n):
    counter=0
    for i in range(n):
        counter+=i+1
    print(counter)
sum(number)
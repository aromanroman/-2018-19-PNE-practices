number_input = int(input("Introduce the number that you want to calculate the nth term of the fibonacci series: "))


def fibonacci(number):
    temporal_fibonacci_list = [0, 1]
    if number==1:
        print("the", number, "th term is ", temporal_fibonacci_list[-2])

    else:

        for n in range(number-2):
            last_element = temporal_fibonacci_list[-1]
            anterior_element = temporal_fibonacci_list[-2]

            counter = last_element + anterior_element
            temporal_fibonacci_list.append(counter)
        print("the",number,"th term is ",temporal_fibonacci_list[-1])


fibonacci(number_input)
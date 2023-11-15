word = 'Johan you are the best!!'


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def prom(number_list):
    N = len(number_list)
    sumatory = 0
    for i in number_list:
        sumatory = sumatory + i
    return sumatory / N


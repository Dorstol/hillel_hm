"""There is a queue for the self-checkout tills at the supermarket. Your task is written a function to calculate the
total time required for all the customers to check out!

input customers: an array of positive integers representing the queue. Each integer represents a customer,
and its value is the amount of time they require to check out. n: a positive integer, the number of checkout tills.
output The function should return an integer, the total time required. """


def queue_time(customers, n):
    if len(customers) > 0:
        if n == 1:
            return sum(customers)
        elif n >= len(customers):
            return max(customers)
        else:
            x = customers[:n]
            for i in customers[n:]:
                y = x.index(min(x))
                x[y] += i
            return max(x)
    return 0


"""
Let us consider this example (array written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.
"""


def parts_sums(ls):
    sum_of_n = sum(ls)
    arr_of_n = [sum_of_n]

    for item in ls:
        sum_of_n -= item
        arr_of_n.append(sum_of_n)

    return arr_of_n

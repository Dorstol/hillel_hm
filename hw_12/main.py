import re
from string import ascii_lowercase


def new_format(string):
    string = int(string)
    return str(f'{string:,}'.format(string).replace(',', '.'))


if __name__ == '__main__':
    assert (new_format("1000000") == "1.000.000")
    assert (new_format("100") == "100")
    assert (new_format("1000") == "1.000")
    assert (new_format("100000") == "100.000")
    assert (new_format("10000") == "10.000")
    assert (new_format("0") == "0")


# 1. https://www.codewars.com/kata/545cedaa9943f7fe7b000048
def is_pangram(s):
    sentence = s
    sentence = re.sub('[^A-Za-z0-9]+', '', sentence).lower()
    exist_arr = []

    for char in sentence:
        if char in ascii_lowercase:
            if char in exist_arr:
                continue
            else:
                exist_arr.append(char)

    if len(ascii_lowercase) == len(exist_arr):
        return True
    else:
        return False


# 2. https://www.codewars.com/kata/5951d30ce99cf2467e000013
import numpy as np


def pythagorean_triple(integers):
    max_value = np.max(integers)
    integers.remove(max_value)
    a, b = integers
    if pow(max_value, 2) == pow(a, 2) + pow(b, 2):
        return True
    else:
        return False


# 3. https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    temp = sorted([int(i) for i in numbers.split()])
    print(temp)
    numbers = f"{temp[len(temp) - 1]} {temp[0]}"
    print(numbers)
    return numbers


# 4. https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
    return (n - 1) % 9 + 1 if n else 0


# 5. https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    odd_int = []
    even_int = []

    for i in integers:
        if i % 2 == 0:
            odd_int.append(i)
        else:
            even_int.append(i)
    if len(odd_int) > len(even_int):
        return even_int[0]
    else:
        return odd_int[0]

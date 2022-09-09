"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

from string import ascii_lowercase


def high(x):
    list_of_char = dict()
    count = 1
    words = x.split()
    data = dict()

    for i in ascii_lowercase:
        list_of_char[i] = count
        count += 1

    for word in words:
        sum = 0
        for letter in word:
            sum += list_of_char[letter]
        data[word] = sum

    print(data.values())

    result = list(data.keys())[list(data.values()).index(max(data.values()))]
    return result


"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, 
if the number is negative, return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once."""


def solution(number):
    if number < 0:
        return 0

    sum = 0

    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
            continue

        if i % 3 == 0:
            sum += i

        if i % 5 == 0:
            sum += i
    return sum


print(solution(16))

"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""


def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    temp = [i for i in sentence if i in vowels]
    return len(temp)


"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case)."""


def to_camel_case(text):
    camel_text = ''
    i = 0
    while i < len(text):
        if text[i] == '-' or text[i] == '_':
            i += 1
            camel_text += text[i].upper()
        else:
            camel_text += text[i]
        i += 1
    return camel_text

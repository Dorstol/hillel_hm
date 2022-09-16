# 1. Задачка с интервью
data = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]


def main(arr):
    abyss = []
    point = 0
    index_of_first_point = 0
    counter = 0
    for i in arr:
        counter += 1
        if point == i:
            abyss.append(arr[index_of_first_point:counter])
        if i > point:
            point = i
            index_of_first_point = arr.index(point)
    result = max([max(i) - min(i) for i in abyss])
    return result


# 2. https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s):
    if len(s) >= 140 or s == "":
        return False

    result = "#"

    for i in s.split():
        result += i.capitalize()

    return result


# 3. https://www.codewars.com/kata/585d7d5adb20cf33cb000235
def find_uniq(arr):
    result = []
    duplicated = []

    for i in arr:
        if i not in result:
            result.append(i)
        else:
            duplicated.append(i)
    for i in result:
        if i in duplicated:
            result.remove(i)

    return result[0]


# 4. https://www.codewars.com/kata/52223df9e8f98c7aa7000062
def rot13(message: str) -> str:
    CLEAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ROT13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    data = dict(zip(ROT13, CLEAR))

    result = []

    for i in message:
        if not i.isalpha():
            result.append(i)
        for k, v in data.items():
            if v == i:
                result.append(k)

    return ''.join(result)


# 5.https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
def beeramid(bonus, price):
    number_of_cans = int(bonus // price)
    i = 1
    levels = 0
    while number_of_cans > 0:
        i += 1
        number_of_cans -= i * i
        levels += 1
        if number_of_cans <= 0:
            return levels
    return levels

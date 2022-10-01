import random
import unittest

import requests


# 1. Custom map iterator
def tmp1(item):
    return item + 'from_func1'


def tmp2(item):
    return item + 'from_func2'


class custom_map:
    def __init__(self, my_dict, func1=None, func2=None):
        self.my_dict = my_dict
        self.dict_keys = list(my_dict.keys())
        self.dict_values = list(my_dict.values())
        self.func_for_keys = func1
        self.func_for_values = func2
        self.count = 0

    def __next__(self):
        if self.func_for_keys and self.func_for_values is not None:
            current = (self.func_for_keys(self.dict_keys[self.count]),
                       self.func_for_values(self.dict_values[self.count]))

            if self.count > len(self.my_dict):
                raise StopIteration
            else:
                self.count += 1

            return current
        else:
            raise StopIteration

    def __iter__(self):
        return self


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.my_map = custom_map(
            {
                '1': 'one',
                '2': 'two',
                '3': 'three'
            },
            func1=tmp1,
            func2=tmp2
        )

    def tearDown(self) -> None:
        del self.my_map

    def test_iter_equals(self):
        self.assertEqual(next(self.my_map), ('1from_func1', 'onefrom_func2'))

    def test_iter_isInstance(self):
        self.assertIsInstance(self.my_map, custom_map)

    def test_iter_index_error(self):
        with self.assertRaises(IndexError):
            for i in range(5):
                next(self.my_map)

    def test_iter_with_None(self):
        with self.assertRaises(StopIteration):
            self.my_map.func_for_keys = None
            next(self.my_map)


# 2. Words unique generator

def words_generator(words_count: int) -> str:
    words_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(words_site)
    WORDS = response.content.splitlines()

    if words_count >= 10_000:
        raise Exception(ValueError, "words count should be less than 10_000")

    for i in range(words_count):
        tmp = WORDS[random.randint(0, len(WORDS))]
        WORDS.remove(tmp)
        yield tmp.decode("utf-8")


a = words_generator(1000)

for x in a:
    print(x)

import random
import requests

# 1. Custom map iterator
Dictionary1 = {'A': 'Alphabet', 'B': 'Beast', 'C': 'Cinema'}


def tmp1(item):
    return item + 'from_func1'


def tmp2(item):
    return item + 'from_func2'


class CustomMap:
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


my_map = CustomMap(Dictionary1, tmp1, tmp2)

for x in my_map:
    print(x)

# 2. Words unique generator
words_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(words_site)
WORDS = response.content.splitlines()


def words_generator(words_count: int) -> str:
    if words_count >= 10_000:
        raise Exception("words count should be less than 10_000")

    for i in range(words_count):
        tmp = WORDS[random.randint(0, len(WORDS))]
        WORDS.remove(tmp)
        yield tmp.decode("utf-8")


a = words_generator(1000)

for x in a:
    print(x)

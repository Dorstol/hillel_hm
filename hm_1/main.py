import functools
import sys
from collections import OrderedDict
import requests


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (*args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache[cache_key]['freq'] += 1
                return deco._cache[cache_key]['value']
            result = f(*args, **kwargs)
            # looking for element with lowest frequency
            if len(deco._cache) >= max_limit:
                min_freq = min(deco._cache.values(), key=lambda x: x['freq'])['freq']
                for k, v in deco._cache.items():
                    if v['freq'] == min_freq:
                        del deco._cache[k]
                        break
            deco._cache[cache_key] = {'value': result, 'freq': 1}
            print('Cached:')
            for key in deco._cache.keys():
                print(key[0])
            print('_' * 20)
            return result

        deco._cache = OrderedDict()

        return deco
    return internal


def mem_count(f):
    @functools.wraps(f)
    def internal(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f'Memory quantity for action: {f.__name__}, bytes: {sys.getsizeof(result)}')
        return result
    return internal


@mem_count
@cache(max_limit=3)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    try:
        res = requests.get(url)
        return res.content[:first_n] if first_n else res.content
    except Exception as e:
        print(e)
        return None


fetch_url('https://www.google.com')
fetch_url('https://www.google.com')
fetch_url('https://www.google.com')
fetch_url('https://www.dou.ua')
fetch_url('https://www.dou.ua')
fetch_url('https://www.dou.ua')
fetch_url('https://www.youtube.com')
fetch_url('https://www.youtube.com')
fetch_url('https://www.youtube.com')
fetch_url('https://www.youtube.com')
fetch_url('https://www.youtube.com')
fetch_url('https://ithillel.ua')
fetch_url('https://ithillel.ua')
fetch_url('https://ithillel.ua')

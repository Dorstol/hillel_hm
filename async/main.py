import asyncio
import json
import os
import random
import string
from asyncio import iscoroutine
import sqlite3

import requests

fut = asyncio.Future


async def get_image():
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(1):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


async def set_future(future):
    responce = requests.get('https://api.github.com/users/Dorstol')
    result = json.loads(responce.content)['public_repos']
    loop.call_soon_threadsafe(future.set_result, result)


async def wait_for_future(future):
    res = future
    print(res)


async def fill_list(lis):
    x = []
    for i in lis:
        x.append(i + 1)
    print(x)
    return x


async def connect_to_db():
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        print("Database created and Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if connection:
            connection.close()
            print("The SQLite connection is closed")
            loop.close()


async def main(loop):
    await asyncio.gather(
        get_image(),
        set_future(fut),
        wait_for_future(fut),
        fill_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        connect_to_db()
    )

print(iscoroutine(connect_to_db()))

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main(loop=loop))
    except KeyboardInterrupt:
        pass

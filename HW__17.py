"""Написать декоратор, который будет кешировать результат выполнения функции.
Запись в кеше должна быть ограничена по времени, т. е. спустя некоторое время перезаписываться.
 Декоратор принимает в качестве единственного keyword only аргумента timeout для записи в секундах.
Требуется учесть параметры, которые может принимать функция.
Декоратор должен логировать события "New record added" и "Old record was overwritten".
Добавить юниттесты.

Пример использования:

@cache(timeout=60)
def func(*args, **kwargs):
    ..."""

from functools import wraps
import time as t
from datetime import datetime, timedelta
import logging
import unittest


class CasherTests(unittest.TestCase):
    def test_degree_val(self):
        data1 = 5
        data2 = 6
        data3 = 7
        result1 = heavy_def(data1)
        result2 = heavy_def(data2)
        result3 = heavy_def(data3)
        self.assertEqual(result1, f'For {data1} = 100000')
        self.assertEqual(result2, f'For {data2} = 1000000')
        self.assertEqual(result3, f'For {data3} = 10000000')
        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertTrue(result3)

    def test_type(self):
        data = 'abc'
        with self.assertRaises(TypeError):
            heavy_def(data)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('Log_HW17.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def casher(*, limit):
    def count_it(function):
        cash = {}

        @wraps(function)
        def wrapper(*args):
            nonlocal cash
            delta = datetime.now() - timedelta(seconds=+limit)
            current_time = datetime.now()
            if cash.get(args) and cash[args][1] > delta:
                logger.debug(f'For {"".join(map(str, args))} cashed {cash[args]}')
                return cash[args][0]
            elif cash.get(args) and cash[args][1] <= delta:
                res = function(*args), current_time
                cash[args] = res
                logger.debug(f'For {"".join(map(str, args))} Old record was overwritten by values {cash[args]}')
                return res[0]
            else:
                res = function(*args), datetime.now()
                cash[args] = res
                logger.debug(f'New record added {res}')
                return res[0]
        return wrapper
    return count_it


@casher(limit=10)
def heavy_def(degree: int):
    t.sleep(4)
    for i in range(10 ** degree):
        i += 1
    return f'For {degree} = {i}'


if __name__ == "__main__":
    unittest.TestCase()
    # print(heavy_def(7))
    # print(heavy_def(4))
    # print(heavy_def(5))
    # print(heavy_def(6))
    # print(heavy_def(7))
    # print(heavy_def(4))
    # print(heavy_def(6))
    # print(heavy_def(5))
    # print(heavy_def(7))
    # print(heavy_def(3))
    # print(heavy_def(3))
    # print(heavy_def(6))


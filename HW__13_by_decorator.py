"""Требуется реализовать менеджер контекста, который позволит нам производить
измерения времени выполнения некоторого блока кода.
Требуется продокументировать классы/методы.

Пример клиентского кода:

>> with timeit():
>>     func1()
>>     func2()
>>     ...
>> It takes 125 sec."""

from contextlib import contextmanager
import time


@contextmanager
def timeit():
    """Measures code execution time"""
    start = time.time()
    yield
    end = time.time()
    print(f'It takes {end - start :.2f} sec.')


def heavy_def(degree):
    for i in range(10 ** degree):
        i += 1
    return i


if __name__ == '__main__':
    with timeit():
        heavy_def(8)
        heavy_def(8)

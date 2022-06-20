"""Требуется реализовать менеджер контекста, который позволит нам производить
измерения времени выполнения некоторого блока кода.
Требуется продокументировать классы/методы.

Пример клиентского кода:

>> with timeit():
>>     func1()
>>     func2()
>>     ...
>> It takes 125 sec."""
import time


class timeit:
    """Measures code execution time"""
    def __enter__(self):
        """captures the beginning of code execution"""
        self.start = time.time()
        return self.start

    def __exit__(self, exp_type, exp_value, traceback):
        """fixes the completion of code execution and displays the total execution time"""
        self.end = time.time()
        print(f'It takes {self.end - self.start :.2f} sec.')


def heavy_def(degree):
    for i in range(10 ** degree):
        i += 1
    return i


if __name__ == '__main__':
    with timeit():
        heavy_def(8)
        heavy_def(8)



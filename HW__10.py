def calls_limit(*, limit):
    def count_it(f):

        def decorator(*args, **kwargs):
            nonlocal limit
            limit -= 1
            if limit < 0:
                raise RuntimeError('Allowed calls exceeded')
            print(f'I can be called {limit} more times')
            return f(*args, **kwargs)

        return decorator

    return count_it


@calls_limit(limit=5)
def func(*args, **kwargs):
    print('Do something')

func()
func()
func()
func()
func()
func()
func()
func()

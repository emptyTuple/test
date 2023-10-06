x = [1, 2]

xi = iter(x)
# while True:
#     try:
#         i = next(xi)
#     except StopIteration:
#         break
#     print(i ** 2)


def sen_range(start, stop):
    def step():
        nonlocal start
        res = start
        start += 1
        return res
    return iter(step, stop)


def counter(start=1):
    while True:
        yield start
        start += 1







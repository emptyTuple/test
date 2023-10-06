from itertools import product, groupby

m = [[0 for _ in range(3)] for _ in range(5)]

for x, y in product(range(5), range(3)):
    m[x][y] = x * y

s = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 6, 9, 12, 22, 15, 7, 5, 0]


def sorted_runs(xs):
    indices_x = range(len(xs) - 1)

    def is_increasing(idx):
        return xs[idx] > 10

    return groupby(indices_x, is_increasing)


for i, v in sorted_runs(s):
    print(i, list(v))

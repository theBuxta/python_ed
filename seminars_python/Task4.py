from itertools import *
from random import randint

k = randint(2, 7)
print(f"k = {k}")

def get_ratios(k):
    ratios = [randint(1, 9) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 9)
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')

ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('task4_1.txt', 'w') as data:
    data.writelines(polynom1)
    data.writelines('\n')
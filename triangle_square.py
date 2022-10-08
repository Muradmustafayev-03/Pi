import time
import numpy as np
from mpmath import mp

mp.dps = 102


def cos(x, precise: bool = False):
    return mp.sqrt(3) / 2 if x == 30 else \
           mp.sqrt((1 + cos(2 * x, True)) / 2) if precise else \
           np.sqrt((1 + cos(2 * x)) / 2)


def sin(x, precise: bool = False):
    return 0.5 if x == 30 else sin(2 * x, precise) / (2 * cos(x, precise))


def compute_pi(precise: bool = False):
    n = 165 if precise else 25
    return 6 * (2.0 ** n) * sin(30 / (2.0 ** n), precise)


t = time.time()
print('precise pi =', str(compute_pi(precise=True))[:-1])
print('time spent:', time.time() - t, 'seconds')

mp.dps = 16
t = time.time_ns()
print('approximate pi =', str(compute_pi()))
print('time spent:', time.time_ns() - t, 'nanoseconds')

# 3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679

import numpy as np
import time


def throw_stone(): return np.random.rand(2) * 2 - 1


def eval_stone(stone): return stone[0] * stone[0] + stone[1] * stone[1] <= 1


def compute(n):
    green = 0

    for _ in range(n):
        if eval_stone(throw_stone()):
            green += 1

    return 4 * green / n


t = time.time()
print(compute(1000000))
print(time.time() - t, 'seconds')

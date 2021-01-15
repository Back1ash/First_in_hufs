import random
import math

def rand_triangle():
    n_first = random.randint(1,9)
    n_second = random.randint(1,9)
    return math.sqrt(n_first**2+n_second**2)

print(f'result = {rand_triangle()}')

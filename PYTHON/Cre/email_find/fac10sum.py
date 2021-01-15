import math

def fac10sum():
    result = 0
    num = 1
    while num<=10:
        fac_tmp = 1
        for x in range(1,num+1):
            fac_tmp *= x
        result += fac_tmp
        num += 1
    return result

print(f"阶乘和:{fac10sum()}")

# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    powerSum = 0
    for digit in str(n):
        powerSum += int(digit) ** p
        p += 1
    k = 1
    kmax = powerSum // n
    while k <= kmax:
        if k * n == powerSum:
            return k
        k += 1
    return -1


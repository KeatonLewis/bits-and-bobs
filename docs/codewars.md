# Code Wars

The plan with this page is to include some little snippets of code from my kata attempts on codewars.com. It's likely not a permanent page since it doesn't do much but I might play with some Heroku tools for executing the code in browser. 
If you're terribly interested you can also check out my Code Wars profile [here](https://www.codewars.com/users/KeatonLewis).

---

[Link to "Playing with Digits!" Kata](https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python)

```python

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

```

[Link to "Detect Pangram" Kata](https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python)

```python

import string

def is_pangram(s):
    for letter in string.ascii_lowercase:
        if letter not in s.lower():
            return False
    return True

```
import math
def is_prime (num):
    if num <= 3:
        if num > 1:
            return True
    if num %6 != 1 and num % 6 != 5:
        return False
    sqrt = int(math.sqrt(num))
    for i in range (5, sqrt + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

print is_prime (13)
print is_prime (23)
print is_prime (27)

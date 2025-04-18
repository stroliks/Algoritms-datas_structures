
def factorial(n):
    if n<=0:
        raise ValueError("число должно быть положительным")
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

print(factorial(-3))
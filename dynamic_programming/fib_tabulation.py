def fib(n):
    if n == 0 or n == 1: return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n):
        table[i+1] += table[i]
        if i + 2 <= n:
            table[i+2] += table[i]
    return table[n]


print(fib(6))   # 8
print(fib(7))   # 13
print(fib(8))   # 21
print(fib(50))  # 12586269025


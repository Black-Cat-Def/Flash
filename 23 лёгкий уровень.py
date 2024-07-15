def f(a, b):
    if a == b: return 1
    if a > b or a % 8 == 0: return 0
    if a < b: return f(a + 23, b) + f(a + 35, b) + f(a * 2, b)


print(f(60, 410))
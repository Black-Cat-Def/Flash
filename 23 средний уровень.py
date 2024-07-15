def f(a, b, c):
    if a == b and c == 8: return 1
    if a > b or (a == b and c != 8): return 0
    if a < b: return f(a + 23, b, c + 1) + f(a + 35, b, c + 1) + f(a * 2, b, c + 1)


print(f(60, 410, 0))
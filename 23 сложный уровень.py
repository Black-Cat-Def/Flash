def f(a, b, c, d):
    if a == b: return 1
    if a > b: return 0
    if a < b and d == 0:
        return f(a + 3 + c, b, c + 5, d) + f(a + 8 + c, b, c + 5, d) + f(a * 2, b, 0, d + 1)
    if a < b and d == 1:
        return f(a + 3 + c, b, c + 5, d) + f(a + 8 + c, b, c + 5, d)


print(f(60, 410, 0, 0))

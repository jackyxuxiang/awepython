def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g=fib(6)
print(type(g))
for x in g:
    print(x)


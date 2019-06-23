# def fib(n):
#    if n == 0:
#        return [0]
#    elif n == 1:
#        return [0,1]
#    else: 
#        fib_ls = fib(n-1)
#        fib_ls.append(fib_ls[-1] + fib_ls[-2])
#        return fib_ls


def fibs():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b

def next_fib(n):
    fib_arr = fib(60)
    for fib in fib_arr:
        if fib == n:
            return n
        elif fib < n:
            _ = fib
        else:
            return fib

result = []
for num in arr:
    result.append(next_fib(num))

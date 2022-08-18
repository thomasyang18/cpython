def f():
    x = 0
    for i in range(0,10):
        for j in range(0,10):
            x += i**j
    return x

print(f())

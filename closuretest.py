def count():
    fs = []
    for i in range(1, 4):
        def f(x):
            return x * x
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()


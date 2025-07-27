def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
    begin:
    end:
    func:
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

for inspect import isgenerator

gen = some_gen(2,4,pow)

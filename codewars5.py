def f1(x): return x*2
def f2(x): return x+2
def f3(x): return x**2

def f4(x): return x.split()
def f5(xs): return [x[::-1].title() for x in xs]
def f6(xs): return "_".join(xs)

def chained(func,input):
    for i in func:
       y = i(input)
       input = y
       print input
    return y
        










chained([f1,f2,f3],4)
    
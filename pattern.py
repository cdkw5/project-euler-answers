def fib(n):
    a=0
    b=1
    fibl = []
    for i in range(2, n+1):
        c=a+b
        a=b
        b=c
        fibl.append(b)
    return fibl

print(fib(532))
# Run this in online pythonn prgramiz

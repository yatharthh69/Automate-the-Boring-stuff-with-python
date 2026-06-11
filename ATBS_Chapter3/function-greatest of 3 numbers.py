def greatest(a,b,c):
    if a>b and b>c:
        return a
    elif a>c and c>b:
        return a
    elif c<b and c>a:
        return b
    elif b>a and a>c:
        return b
    elif c>a and a>b:
        return c
    else:
        return c
print(greatest(1,2,3))
print(greatest(5,4,2))
print(greatest(1,2,0))
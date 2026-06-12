def fibonacci(n):
    a=0
    b=1
    count=0
    while count!=n:
        print(a)
        temp=a+b
        a=b
        b=temp
        
        count+=1
    return f'Done'
print(fibonacci(1000))
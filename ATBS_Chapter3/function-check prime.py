def isprime(n):
    count=0
    for i in range(1,n+1):
        rem=n%i
        if rem==0:
            count+=1
    if count==2:
        return f"Prime"
    else:
        return f"Composite"
print(isprime(9))
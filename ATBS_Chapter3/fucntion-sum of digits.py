def digsum(n):
    total=0
    while n>0:
        last_dig=n%10
        total=total+last_dig
        n=n//10
    return total
print(digsum(12345))
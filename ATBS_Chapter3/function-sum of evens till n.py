def even_sum(n):
    sum=0
    for i in range(0,n+1,2):
        sum=sum+i
    return sum
print(even_sum(5))
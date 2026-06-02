n=int(input("Enter a number to print prime numbers till that number: "))
for x in range(2,n+1):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        print(x)

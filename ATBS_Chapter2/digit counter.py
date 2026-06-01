n=int(input("Enter any number: "))
count=0
while True:
    n=n//10
    count+=1
    
    if n==0:
        break
print(count)
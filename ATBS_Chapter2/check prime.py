n=int(input("Enter a number to check if prime: "))
total=0
if n>0:
    for i in range(1,n+1):
        if n%i==0:
            total+=1
if total==2:
    print("Number is prime")
else: 
    print("Number is not prime")
  
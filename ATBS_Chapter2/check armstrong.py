n=int(input("Enter a number: "))
count=n
number=n
digits=0
while True:
    count=count//10
    digits=digits+1
    if count==0:
        break   
sum=0
while True:
    rem=n%10
    sum=sum+rem**digits
    n=n//10
    if n==0:
        break
if sum==number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
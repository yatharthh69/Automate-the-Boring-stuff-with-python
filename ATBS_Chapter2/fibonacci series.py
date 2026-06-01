term=int(input("Enter number of terms: "))
a=0
b=1
count=0
while count<=term:
    print(a)
    temp=a+b
    a=b
    b=temp
    count+=1

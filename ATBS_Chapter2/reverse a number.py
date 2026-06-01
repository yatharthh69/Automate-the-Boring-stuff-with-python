n=int(input("Enter a number to reverse: "))
new_num=0
while True:
    lastdig=n%10
    new_num=new_num*10+lastdig
    n=n//10
    if n==0:
        break
print(new_num)
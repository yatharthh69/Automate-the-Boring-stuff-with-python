n=int(input("Enter a number to reverse: "))
actual_number=n
new_num=0
while True:
    lastdig=n%10
    new_num=new_num*10+lastdig
    n=n//10
    if n==0:
        break
if new_num==actual_number:
    print("Number is Palindrome")
else:
    print("Number isn't Palindrome")
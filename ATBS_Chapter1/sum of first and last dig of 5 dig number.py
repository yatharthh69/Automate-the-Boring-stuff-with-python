num=int(input("Enter a five digit number:"))
firstdigit=num%10
lastdigit=num//10000
print(firstdigit+lastdigit)
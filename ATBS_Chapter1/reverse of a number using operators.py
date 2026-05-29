num=int(input("Enter any three digit number: "))
ones=num%10
tens=(num//10)%10
hund=num//100
number=ones*100+tens*10+hund
print(number)
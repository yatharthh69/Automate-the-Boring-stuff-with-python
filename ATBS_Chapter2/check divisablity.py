num=int(input("Enter a number: "))
if num%3==0 and num%5 ==0:
    print("Number is divisible by both 3 and 5")
elif num%3==0 and num%5!=0:
    print("Number is divisible by 3 but not by 5")
elif num%3!=0 and num%5==0:
    print("Number is not divisible by 3 but is divisible by 5")
elif num==0:
    print("Number is zero")
else:
    print("Number is not divisible by both 3 and 5")
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if num1>num2 and num2>num3:
    print("First number is greatest of all and second is greater than third")
elif num1>num3 and num3>num2:
    print("First is greatest of all and third is greater than second")
elif num3<num2 and num3>num1:
   print("Second is greatest of all and third greater than first")
elif num2>num1 and num1>num3:
    print("Second is greatest of all first is greater than third")
elif num3>num1 and num1>num2:
    print("Third is greatest of all and first is greater than second")
else:
    print("Third is greatest of all and second is greater than first")
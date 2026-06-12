def  divide(dividend,divisor):
    try:
        return dividend/divisor
    except ZeroDivisionError:
       return f"Can't divide a number by 0"
print(divide(4,2))
print(divide(2,4))
print(divide(0,1))
print(divide(1,0))
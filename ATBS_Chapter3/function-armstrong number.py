def armstrong_check(n):
    actual_num=n
    digit_count_number=n
    digit=0
    while digit_count_number>0:
        digit_count_number=digit_count_number//10
        digit+=1
    sum=0
    while n>0:
        sum=sum+(n%10)**digit
        n=n//10
    if sum==actual_num:
        return f"Armstrong number"
    else:
        return f"Not an Armstrong number"
print(armstrong_check(8208))
print(armstrong_check(8802))
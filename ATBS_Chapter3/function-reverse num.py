def reverse(n):
    reverse=0
    while n>0:
        last_dig=n%10
        reverse=reverse*10+last_dig
        n=n//10
    return reverse
print(reverse(98765432123456789))
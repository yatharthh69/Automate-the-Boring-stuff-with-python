def is_palindrome(n):
    number=n
    reverse=0
    while number>0:
        last_dig=number%10
        reverse=reverse*10+last_dig
        number=number//10
    if reverse==n:
        return f"Palindrome Number"
    else:
        return f"Not Palindrome"
print(is_palindrome(12221))
print(is_palindrome(123123123333333))
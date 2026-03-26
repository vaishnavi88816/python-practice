def palindrome(str):
    rev=""
    for i in range (len(str)-1,-1,-1):
        rev=rev+str[i]
    if rev==str:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")
palindrome("NAMAN")
palindrome("CURSOR")        
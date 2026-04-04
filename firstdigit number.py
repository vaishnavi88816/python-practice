def firstDigit():
    n=int(input("print a number:"))
    while n>=9:
        n=n//10
    print(n)
firstDigit()
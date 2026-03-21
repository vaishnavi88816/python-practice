def add(a,b):
   return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
   return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "cannot divide by zero"
a= int(input("enter first number"))
b= int(input("enter second number"))
print("add:",add(a,b))
print("substraction:",subtract(a,b))
print("multiply:",multiply(a,b))
print("divide:",divide(a,b))

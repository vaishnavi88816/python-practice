n=int(input("print a number:"))
def pos(n):
    n -= 1
    while n >= 0:
        print(n, end=' ')
        n-=1
        
    
def neg(n):
    
    while n <= 0:
        print(n, end=' ')
        n += 1
if n == 0:
        print("already Zero")
elif n > 0:
        pos(n)
else:
        neg(n)


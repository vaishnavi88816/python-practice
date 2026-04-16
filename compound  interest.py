p = int(input("Principal amount:-"))  
r = int(input("Rate of interest:-"))          
t = int(input("Time in years:-"))           

Amt = p
for i in range(t):
    Amt = Amt * (1 + r / 100)

CI = Amt - p
print("Compound interest:", CI)
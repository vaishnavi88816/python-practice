balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount % 100 != 0 or amount % 500 != 0:
    print("Enter amount in multiples of 100")

elif amount > balance:
    print("Insufficient balance")

else:
    balance = balance - amount
    print("Transaction successful")
    print("Remaining balance:", balance)
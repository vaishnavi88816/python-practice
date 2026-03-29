total = 0
n = int(input("Enter number of items: "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    total += price

print("Total amount before discount:", total)


if total >= 2000:
    discount = total * 0.20
elif total >= 1000:
    discount = total * 0.10
elif total >= 500:
    discount = total * 0.05
else:
    discount = 0


if discount > 0:
    print("🎉 Congrats! You got a discount of", discount)
else:
    print("❌ No discount applied. Shop more to get a discount!")

final_amount = total - discount

print("Final amount to pay:", final_amount)

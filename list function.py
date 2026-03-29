# list_basics.py

def list_operations():
    numbers = [10, 20, 30, 40, 50]

    print("Original List:", numbers)

    numbers.append(60)
    print("After Append:", numbers)

    numbers.remove(20)
    print("After Remove:", numbers)

    numbers.sort(reverse=True)
    print("Sorted Desc:", numbers)
    
list_operations()
    
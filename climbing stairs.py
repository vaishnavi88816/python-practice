def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second


# Driver Code
n = int(input("Enter number of stairs: "))
print("Number of ways =", climb_stairs(n))
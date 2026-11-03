# Write a recursive function that prints numbers from 1 to N.
def print_numbers(n):
    # Base Case: Stop the recursion when n becomes 0
    if n == 0:
        return
    
    # Recursive Call: Move closer to the base case first
    print_numbers(n - 1)
    
    # Action: Print the current number on the way back up
    print(n, end=" ")

# Example usage:
# Call the function to print from 1 to 5
n=int(input("enter a number:"))
print_numbers(n)




## Write a recursive function that prints numbers from 1 to N.
def print_numbers(n):
    # Base Case: Stop the recursion when n becomes 0
    if n == 0:
        return
    # Action: Print the current number on the way back up
    print(n, end=" ")
    
    # Recursive Call: Move closer to the base case first
    print_numbers(n - 1)
    # Example usage:
# Call the function to print from n to 1
n=int(input("enter a number:"))
print_numbers(n)



# 2. Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 1 or n==0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))




# 3. Write a recursive function to print the Fibonacci series up to N terms.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(6):
    print(fibonacci(i), end=" ")



#Write both a recursive and iterative function to find factorial - compare results.
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_iterative(5))
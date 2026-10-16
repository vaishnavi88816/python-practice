"""
Problem: Remove Duplicates from Sorted Array

Description:
Given a sorted array, remove duplicate elements so that
each element appears only once.

Example:
Input:  [1, 1, 2, 2, 3, 4, 4]
Output: [1, 2, 3, 4]

Approach:
Use two pointers to modify the array in-place.

Time Complexity: O(n)
Space Complexity: O(1) extra space for the algorithm
"""


def remove_duplicates(numbers):
    # Handle an empty array
    if not numbers:
        return 0

    # Position where the next unique element will be placed
    write = 1

    # Check elements starting from the second position
    for read in range(1, len(numbers)):

        # Compare the current element with the last unique element
        if numbers[read] != numbers[write - 1]:

            # Place the unique element at the write position
            numbers[write] = numbers[read]

            # Move to the next position
            write += 1

    # Return the number of unique elements
    return write


# Take input from the user
numbers = list(map(int, input("Enter sorted array elements: ").split()))

# Remove duplicates
unique_count = remove_duplicates(numbers)

# Display only the unique elements
print("Array after removing duplicates:", numbers[:unique_count])
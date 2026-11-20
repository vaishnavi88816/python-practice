# 1. Largest aur Smallest Element nikalna
def find_min_max(arr):
    return min(arr), max(arr)

# 2. Array ko Reverse karna (Two-Pointer Approach)
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# 3. Duplicate Elements hatana
def remove_duplicates(arr):
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)
    return unique

# 4. Second Largest Element find karna
def second_largest(arr):
    unique_nums = list(set(arr))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

# 5. Two Sum Problem (Target sum ke indices nikalna)
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# --- Main Program ---
if __name__ == "__main__":
    numbers = [10, 25, 7, 42, 18, 25, 42]
    
    print("Original Array:", numbers)
    print("Min & Max:", find_min_max(numbers))
    print("Second Largest:", second_largest(numbers))
    print("Without Duplicates:", remove_duplicates(numbers))
    print("Two Sum (Target 32) Indices:", two_sum(numbers, 32))
    print("Reversed Array:", reverse_array(numbers.copy()))

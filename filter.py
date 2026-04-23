# filter_program.py

# Example 1: Even numbers filter
numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# Example 2: Numbers greater than 20
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print("Numbers > 20:", greater_than_20)


# Example 3: Filter names starting with 'A'
names = ["Aman", "Rahul", "Ankit", "Suresh"]
names_with_A = list(filter(lambda name: name.startswith('A'), names))
print("Names starting with A:", names_with_A)


# Example 4: Filter students who passed (marks >= 40)
students_marks = [35, 67, 80, 20, 45]
passed_students = list(filter(lambda m: m >= 40, students_marks))
print("Passed students:", passed_students)
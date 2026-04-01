name = input("Enter student name: ")

mathematics = int(input("Enter marks of mathematics: "))
chemistry = int(input("Enter marks of chemistry: "))
physics = int(input("Enter marks of physics: "))
english = int(input("Enter marks of english: "))
computer = int(input("Enter marks of computer: "))
total=500
obtained_marks = mathematics + chemistry + physics + english + computer
percentage = (obtained_marks / total)*100

print("\n----- Result -----")
print("Name:", name)
print("obtained_Marks:", obtained_marks)
print("total marks:", total)
print("Percentage:", percentage, "%")

# Grade Calculation
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
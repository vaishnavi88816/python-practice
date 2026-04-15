students={}
"""n=int(input("enter number of total students:"))
for i in range(n):
    name=input("enter student name:-")
    marks=int(input("enter marks:-"))
    students[name]=marks"""
while True:
    print("enter your choices")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. show Result")
    print("5. Exit")
    choice = int(input("your choice is:"))
    if choice==1:
        name=input(("Enter a name:"))
        marks=int(input("Enter marks:"))
        students[name]=marks
    elif choice==2:
        name=input("Enter name to update:")
        if name in students:
            students[name]=int(input("Enter new marks:"))
        else:
            print("student not found")
    elif choice == 3:
        name=input("Enter name to delete:")
        if name in students:
            students.pop(name)
        else:
            print("student not found")
    elif choice == 4:
        if students:
            print("All Students:",students)
            total=sum(students.values())
            avg=total/len(students)
            max_students = max(students,key=students.get)
            min_students = min(students,key=students.get)
            print("Total Marks:",total)
            print("Average Marks:",avg)
            print("Topper:",max_students)
            print("Lowest:",min_students)
        else:
            print("No Data Available")
    elif choice == 5:
        break
    else:
        print("invalid choice")
                
                
                
               
   
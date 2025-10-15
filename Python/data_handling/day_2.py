
name_marks = {}

def stu_marks(name , marks):
    if name in name_marks :
        print("The student already exists . Try different name.\n")
    else:
        name_marks[name] = marks
        print(f"{name} added successfully!\n")

while True :
    name = input("Enter student name(or enter 'done' to stop): ").strip()

    if name.lower() == "done" :
        print("Thanks! Input complete. \n")
        break

    marks = int(input(f"Enter marks for {name}: "))    

    stu_marks(name , marks)


if name_marks:  
    total_sum = sum(name_marks.values())
    total_students = len(name_marks)
    avg = total_sum / total_students

    highest_marks = max(name_marks.values())
    lowest_marks = min(name_marks.values())

    top_students = [student for student, mark in name_marks.items() if mark == highest_marks]
   
    bottom_students = [student for student, mark in name_marks.items() if mark == lowest_marks]

   
    print("========== Student Marks Report ==========")
    print(f"Total number of students: {total_students}")
    print(f"Average marks: {avg:.2f}\n")
    print(f"Highest marks: {highest_marks} — {', '.join(top_students)}")
    print(f"Lowest marks: {lowest_marks} — {', '.join(bottom_students)}")
    print("=========================================")
else:
    print("No student data entered.")



 

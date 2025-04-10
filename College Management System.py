class person:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(rollno, name)
        self.branch = branch

class teacher(person):
    def __init__(self, rollno, name, subject):
        super().__init__(rollno, name)
        self.subject = subject

class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        for i, student in enumerate(self.students, start=1):
            print(f"Student {i}:")
            print(f"Roll Number: {student.rollno}")
            print(f"Name : {student.name}")
            print(f"Branch: {student.branch}")
            print()

    def display_teachers(self):
        if not self.teachers:
            print("No teachers found.")
            return
        for i, teacher in enumerate(self.teachers, start=1):
            print(f"Teacher {i}:")
            print(f"Roll Number: {teacher.rollno}")
            print(f"Name : {teacher.name}")
            print(f"Subject: {teacher.subject}")
            print()

    def find_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                return student
        return None

    def find_teacher(self, rollno):
        for teacher in self.teachers:
            if teacher.rollno == rollno:
                return teacher
        return None

colleges = []

while True:
    print("Choose the Required option: ")
    print("1. Create College.")
    print("2. Add Student.")
    print("3. Add Teacher.")
    print("4. Display Students.")
    print("5. Display Teachers.")
    print("6. Exit.")
    print("7. Find Student.")
    print("8. Find Teacher.")

    try:
        x = int(input("Enter your Option: "))
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        continue

    if x == 1:
        clgname = input("Enter College Name: ")
        if any(clg.cname == clgname for clg in colleges):
            print("\nCollege Already Exists!\n")
        else:
            colleges.append(college(clgname))
            print("\nCollege Added Successfully\n")

    elif x == 2:
        clgname = input("Enter College Name: ")
        clg = next((clg for clg in colleges if clg.cname == clgname), None)
        if clg:
            rollno = input("Enter Roll no: ")
            name = input("Enter Student Name: ")
            branch = input("Enter Student Branch: ")
            s1 = student(rollno, name, branch)
            clg.add_student(s1)
            print("\nStudent Added Successfully\n")
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 3:
        clgname = input("Enter College Name: ")
        clg = next((clg for clg in colleges if clg.cname == clgname), None)
        if clg:
            rollno = input("Enter Rollno: ")
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            t1 = teacher(rollno, name, subject)
            clg.add_teacher(t1)
            print("\nTeacher Added Successfully!\n")
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 4:
        clgname = input("Enter College Name: ")
        clg = next((clg for clg in colleges if clg.cname == clgname), None)
        if clg:
            print()
            clg.display_students()
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 5:
        clgname = input("Enter College Name: ")
        clg = next((clg for clg in colleges if clg.cname == clgname), None)
        if clg:
            print()
            clg.display_teachers()
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 6:
        print("\nExiting... Goodbye!\n")
        break

    elif x == 7:
        clgname = input("Enter College Name: ")
        clg = next((clg for clg in colleges if clg.cname == clgname), None)
        if clg:
            rollno = input("Enter Roll Number of the Student to Find: ")
            student = clg.find_student(rollno)
            if student:
                print("\nStudent Found!")
                print(f"Roll Number: {student.rollno}")
                print(f"Name       : {student.name}")
                print(f"Branch     : {student.branch}\n")
            else:
                print("\nStudent Not Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 8:
        clgname = input("Enter College Name: ")
        clg = next((clg for clg in colleges if clg.cname == clgname), None)
        if clg:
            rollno = input("Enter Roll Number of the Teacher to Find: ")
            teacher = clg.find_teacher(rollno)
            if teacher:
                print("\nTeacher Found!")
                print(f"Roll Number: {teacher.rollno}")
                print(f"Name       : {teacher.name}")
                print(f"Subject    : {teacher.subject}\n")
            else:
                print("\nTeacher Not Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")

    else:
        print("\nChoose a Correct Option!\n")

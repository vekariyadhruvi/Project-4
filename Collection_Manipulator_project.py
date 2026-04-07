students=[]
subjects_offered= set()

print("WELCOME to the STUDENT DATA ORGANIZER:)")

while True:
    print("\nSelect an option from below:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice=int(input("\nEnter your choice:"))

    if choice==1:
        print("\nEnter student details:")
        sid=int(input("Student ID:"))
        name=input("Name:")
        age=int(input("Age:"))
        grade=input("Grade:")
        dob=input("Date of Birth(DD-MM-YYYY):")
        tup=(sid, dob)

        sub=input("Subjects (comma-separated):")
        subjects=[s.strip() for s in sub.split(",")]
        subjects_offered.update(subjects)

        student={
            "id":tup,
            "name":name,
            "age":age,
            "grade": grade,
            "subjects":subjects
        }

        students.append(student)
        print("Student added successfully!")
   
    elif choice==2:
        print("\n---Display All Students---")
        for s in students:
            print(f"Student ID: {s["id"][0]} | Name: {s["name"]} | Age: {s["age"]} | Grade: {s["grade"]} | Subjects: {', '.join(s["subjects"])} ")

    elif choice==3:
        sid=int(input("\nEnter Student ID to be updated:"))
        found=False
        for i in students:
            if i["id"][0]==sid:
                i["age"]=int(input("Enter new Age:"))
                i["grade"]=input("Enter new Grade:")
                print("Student ID updated successfully!")
                found=True
                break
        if not found:
            print("Student ID not found")

    elif choice==4:
        sid=int(input("\nEnter Student ID to be deleted:"))
        found=False
        for i in range(len(students)):
            if students[i]["id"][0]==sid:
                del students[i]
                print("Student ID successfully deleted!")
                found=True
                break
        if not found:
            print("Student ID not found")

    elif choice==5:
        print("\nSUBJECTS OFFERED are:")
        for i in subjects_offered:
                print(i)

    elif choice==6:
        print("Exiting the program. THANK YOU!")
        break

    else:
        print("Invalid option. Choose again")
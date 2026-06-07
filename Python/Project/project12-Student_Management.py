# Project 12: Student Management

import os

class Student:
    def __init__(self, student_id, name, roll, department):
        self.student_id = student_id
        self.name = name
        self.roll = roll
        self.department = department

    def to_string(self):
        # ফাইল এ সেভ করার ফরম্যাট তৈরি
        return f"{self.student_id},{self.name},{self.roll},{self.department}"


class SMSManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self, student):
        with open(self.filename, "a") as file:
            file.write(student.to_string() + "\n")
        print(f"🎉 Student '{student.name}' added and saved successfully!")

    def display_all_students(self):
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            print("\n📭 No student records found.")
            return
        
        print("\n" + "="*50)
        print(f"{'ID':<10} {'Name':<15} {'Roll':<10} {'Department':<15}")
        print("="*50)
        
        with open(self.filename, "r") as file:
            for line in file:
                if line.strip():
                    s_id, name, roll, dept = line.strip().split(',')
                    print(f"{s_id:<10} {name:<15} {roll:<10} {dept:<15}")
        print("="*50)

    def search_student(self, student_id):
        if not os.path.exists(self.filename):
            print("No records available.")
            return
        
        found = False
        with open(self.filename, "r") as file:
            for line in file:
                if line.strip():
                    s_id, name, roll, dept = line.strip().split(',')
                    if s_id == student_id:
                        print("\n🔍 Student Found:")
                        print(f"ID: {s_id}\nName: {name}\nRoll: {roll}\nDepartment: {dept}")
                        found = True
                        break
        if not found:
            print(f"Student with ID {student_id} not found.")


def main():
    manager = SMSManager()
    
    while True:
        print("\n--- Student Management System (SMS) ---")
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Exit")
        
        choice = input("Enter option (1-4): ")
        
        if choice == '1':
            print("\n--- Enter Student Details ---")
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            roll = input("Enter Student Roll: ").strip()
            dept = input("Enter Department: ").strip()
            
            if s_id and name and roll and dept:
                new_student = Student(s_id, name, roll, dept)
                manager.add_student(new_student)
            else:
                print("⚠ All fields are required!")
                
        elif choice == '2':
            manager.display_all_students()
            
        elif choice == '3':
            search_id = input("Enter Student ID to search: ").strip()
            manager.search_student(search_id)
            
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Choose between 1 and 4.")

if __name__ == "__main__":
    main()
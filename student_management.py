import json
import os

# Student Class
class Student:
    def __init__(self, name, roll_no, marks1, marks2):
        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2

    def to_dict(self):
        # Convert Student Object to Dictionary
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks1': self.marks1,
            'marks2': self.marks2
        }


# Student Management System Class
class StudentManagementSystem:
    def __init__(self, file_name='student.json'):
        self.file_name = file_name
        self.students = self.load_data()

    def menu(self):
        while True:
            choice = input('''
                    ===== Student Management System =====
                    1. Accept Student Details
                    2. Display All Students
                    3. Search Student by Roll No
                    4. Delete Student Record
                    5. Update Roll No
                    6. Exit
                    Enter your choice: 
                    ''')
            print()

            if choice == "1":
                name = input("Enter name: ")
                roll_no = input("Enter roll number: ")
                marks1 = int(input("Enter marks for subject 1: "))
                marks2 = int(input("Enter marks for subject 2: "))
                self.accept(name, roll_no, marks1, marks2)

            elif choice == "2":
                self.display_all()

            elif choice == "3":
                roll_no = input("Enter roll number to search: ")
                self.search(roll_no)

            elif choice == "4":
                roll_no = input("Enter roll number to delete: ")
                self.delete(roll_no)

            elif choice == "5":
                old_roll = input("Enter old roll number: ")
                new_roll = input("Enter new roll number: ")
                self.update(old_roll, new_roll)

            elif choice == "6":
                print("Exiting Student Management System. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.\n")

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.students, file, indent=4)

    def accept(self, name, roll_no, marks1, marks2):
        student = Student(name, roll_no, marks1, marks2)
        self.students.append(student.to_dict())
        self.save_data()
        print("Student record added successfully.\n")

    def display_all(self):
        if not self.students:
            print('No student records found.\n')
            return
        print('\nAll Student Records:')
        for st in self.students:
            print(f"Name: {st['name']}, \nRoll No: {st['roll_no']}, \nMarks1: {st['marks1']}, \nMarks2: {st['marks2']}")
        print()

    def search(self, roll_no):
        for stu in self.students:
            if stu['roll_no'] == roll_no:
                print("\nStudent Found:")
                print(f"Name: {stu['name']}, \nRoll No: {stu['roll_no']}, \nMarks1: {stu['marks1']}, \nMarks2: {stu['marks2']}\n")
                return
        print("Student not found.\n")

    def delete(self, roll_no):
        for stu in self.students:
            if stu['roll_no'] == roll_no:
                self.students.remove(stu)
                self.save_data()
                print("Student record deleted successfully.\n")
                return
        print("Student record not found.\n")

    def update(self, old_roll_no, new_roll_no):
        for stu in self.students:
            if stu['roll_no'] == old_roll_no:
                stu['roll_no'] = new_roll_no
                self.save_data()
                print("Roll number updated successfully.\n")
                return
        print("Student not found!\n")



if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()

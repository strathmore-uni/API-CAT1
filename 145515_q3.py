class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_ID = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print("Salary of {self.name} has been updated to ${self.salary:.2f}")

class Department:
    def __init__(self, department_name, employees):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.department_name} department.")

    def total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department is: ${total_salary:.2f}")

    def display_all_employees(self):
        if not self.employees:
            print(f"No employees in the {self.department_name} department.")
        else:
            print(f"Employees in {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()

if __name__ == "__main__":
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nMenu:")
        print("1. Add an employee")
        print("2. Display total salary expenditure")
        print("3. Display all employees")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            salary = float(input("Enter employee's salary: "))
            
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            department.total_salary_expenditure()

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
        
        
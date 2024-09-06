import json

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

class DepartmentSummary:
    def __init__(self, department):
        self.department = department
        self.employees = []

    def add_employee(self, employee):
        if employee.department == self.department:
            self.employees.append(employee)

    def calculate_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def to_dict(self):
        return {
            'department': self.department,
            'average_salary': self.calculate_average_salary(),
            'employee_count': len(self.employees)
        }

def read_employees(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [Employee(emp['name'], emp['department'], emp['salary']) for emp in data['employees']]

def save_summary(summary, output_file):
    with open(output_file, 'w') as file:
        json.dump(summary, file, indent=4)

def main():
    input_file = 'employees.json'
    output_file = 'department_summary.json'
    department = 'Engineering'

    employees = read_employees(input_file)
    summary = DepartmentSummary(department)
    
    for emp in employees:
        summary.add_employee(emp)
    
    summary_data = summary.to_dict()
    save_summary(summary_data, output_file)
    print(f"Department summary saved to {output_file}")

if __name__ == "__main__":
    main()

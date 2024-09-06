import json

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
    return content['employees']

def get_employees_by_department(employees, department):
    filtered = []
    for employee in employees:
        if employee['department'] == department:
            filtered.append(employee)
    return filtered

def average_salary(employees):
    if not employees:
        return 0
    total_salary = sum(emp['salary'] for emp in employees)
    avg_salary = total_salary / len(employees)
    return avg_salary

def write_json_output(results, output_file):
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)

def main():
    input_file = 'employees.json'
    output_file = 'department_summary.json'
    department = 'Engineering'

    employees = load_json_file(input_file)
    department_employees = get_employees_by_department(employees, department)
    avg_salary = average_salary(department_employees)
    output_data = {
        'department': department,
        'average_salary': avg_salary,
        'employee_count': len(department_employees)
    }

    write_json_output(output_data, output_file)
    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    main()

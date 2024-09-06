import json

def fetch_employee_data(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data['employees']

def filter_by_department(employees, dept):
    return [emp for emp in employees if emp['department'] == dept]

def compute_average_salary(employees):
    if not employees:
        return 0
    total = sum(emp['salary'] for emp in employees)
    return total / len(employees)

def write_results_to_json(results, output_file):
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)

def main():
    input_file = 'employees.json'
    output_file = 'department_summary.json'
    department = 'Engineering'

    employees = fetch_employee_data(input_file)
    dept_employees = filter_by_department(employees, department)
    avg_salary = compute_average_salary(dept_employees)
    summary = {
        'department': department,
        'average_salary': avg_salary,
        'employee_count': len(dept_employees)
    }

    write_results_to_json(summary, output_file)
    print(f"Data written to {output_file}")

if __name__ == "__main__":
    main()

import json

def read_employee_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['employees']

def filter_employees_by_department(employees, department):
    return [employee for employee in employees if employee['department'] == department]

def calculate_average_salary(employees):
    total_salary = sum(employee['salary'] for employee in employees)
    return total_salary / len(employees) if employees else 0

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)

def main():
    input_file = 'employees.json'
    output_file = 'department_summary.json'
    department = 'Engineering'

    employees = read_employee_data(input_file)
    filtered_employees = filter_employees_by_department(employees, department)
    average_salary = calculate_average_salary(filtered_employees)
    results = {
        'department': department,
        'average_salary': average_salary,
        'employee_count': len(filtered_employees)
    }

    save_results_to_json(results, output_file)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()

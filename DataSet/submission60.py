import json

def get_employees_from_json(filepath):
    with open(filepath, 'r') as f:
        content = json.load(f)
    return content['employees']

def select_employees(employees, dept):
    selected_employees = []
    for employee in employees:
        if employee['department'] == dept:
            selected_employees.append(employee)
    return selected_employees

def avg_salary_calculator(employees):
    if not employees:
        return 0
    total_salaries = sum(emp['salary'] for emp in employees)
    average = total_salaries / len(employees)
    return average

def output_json_data(data, output_filepath):
    with open(output_filepath, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    input_file = 'employees.json'
    output_file = 'department_summary.json'
    dept = 'Engineering'

    employees = get_employees_from_json(input_file)
    employees_in_dept = select_employees(employees, dept)
    average_salary = avg_salary_calculator(employees_in_dept)
    
    summary = {
        'department': dept,
        'average_salary': average_salary,
        'employee_count': len(employees_in_dept)
    }

    output_json_data(summary, output_file)
    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    main()

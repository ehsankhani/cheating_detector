import json

def load_employees(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['employees']

def is_in_department(department):
    def inner(employee):
        return employee['department'] == department
    return inner

def get_salary(employee):
    return employee['salary']

def calculate_average(salaries):
    if not salaries:
        return 0
    return sum(salaries) / len(salaries)

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    input_file = 'employees.json'
    output_file = 'department_summary.json'
    department = 'Engineering'

    employees = load_employees(input_file)
    department_employees = list(filter(is_in_department(department), employees))
    salaries = list(map(get_salary, department_employees))
    avg_salary = calculate_average(salaries)
    
    result = {
        'department': department,
        'average_salary': avg_salary,
        'employee_count': len(department_employees)
    }

    save_to_json(result, output_file)
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    main()

import csv

def read_student_scores(file_path):
    students = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {
                'name': row['Name'],
                'score': float(row['Score'])
            }
            students.append(student)
    return students

def calculate_average_score(students):
    total_score = sum(student['score'] for student in students)
    average_score = total_score / len(students)
    return average_score

def assign_grades(students, average_score):
    for student in students:
        if student['score'] >= average_score:
            student['grade'] = 'A'
        else:
            student['grade'] = 'B'
    return students

def write_results_to_csv(students, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Score', 'Grade'])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def main():
    input_file = 'students.csv'
    output_file = 'graded_students.csv'
    students = read_student_scores(input_file)
    average_score = calculate_average_score(students)
    students_with_grades = assign_grades(students, average_score)
    write_results_to_csv(students_with_grades, output_file)
    print(f"Processed student data written to {output_file}")

if __name__ == "__main__":
    main()

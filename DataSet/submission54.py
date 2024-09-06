import csv

def load_student_scores(filepath):
    all_students = []
    with open(filepath, mode='r') as file:
        csv_data = csv.DictReader(file)
        for line in csv_data:
            all_students.append({'name': line['Name'], 'score': float(line['Score'])})
    return all_students

def avg_score_calculator(students):
    total_scores = sum(student['score'] for student in students)
    avg_score = total_scores / len(students)
    return avg_score

def grade_students(students, avg):
    for student in students:
        student['grade'] = 'A' if student['score'] >= avg else 'B'
    return students

def save_results_to_csv(students, output_filepath):
    with open(output_filepath, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Score', 'Grade'])
        writer.writeheader()
        writer.writerows(students)

def main():
    input_csv = 'students.csv'
    output_csv = 'graded_students.csv'
    students_list = load_student_scores(input_csv)
    average = avg_score_calculator(students_list)
    graded_students = grade_students(students_list, average)
    save_results_to_csv(graded_students, output_csv)
    print(f"Graded students data saved to {output_csv}")

if __name__ == "__main__":
    main()

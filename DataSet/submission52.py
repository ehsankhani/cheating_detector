import csv

def fetch_student_scores(file_path):
    student_data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for record in csv_reader:
            student_data.append({
                'name': record['Name'],
                'score': float(record['Score'])
            })
    return student_data

def compute_average(student_data):
    total = sum(s['score'] for s in student_data)
    return total / len(student_data)

def determine_grades(student_data, avg_score):
    for s in student_data:
        if s['score'] >= avg_score:
            s['grade'] = 'A'
        else:
            s['grade'] = 'B'
    return student_data

def export_results(student_data, output_file):
    with open(output_file, 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=['Name', 'Score', 'Grade'])
        csv_writer.writeheader()
        csv_writer.writerows(student_data)

def main():
    input_file = 'students.csv'
    output_file = 'graded_students.csv'
    student_data = fetch_student_scores(input_file)
    avg_score = compute_average(student_data)
    graded_students = determine_grades(student_data, avg_score)
    export_results(graded_students, output_file)
    print(f"Graded data exported to {output_file}")

if __name__ == "__main__":
    main()

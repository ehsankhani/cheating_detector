import csv

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = None

    def assign_grade(self, average_score):
        self.grade = 'A' if self.score >= average_score else 'B'

class StudentProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.students = []

    def read_students(self):
        with open(self.input_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row['Name'], float(row['Score']))
                self.students.append(student)

    def calculate_average(self):
        total_score = sum(student.score for student in self.students)
        return total_score / len(self.students)

    def grade_students(self, average_score):
        for student in self.students:
            student.assign_grade(average_score)

    def write_results(self, output_file):
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Score', 'Grade'])
            for student in self.students:
                writer.writerow([student.name, student.score, student.grade])

def main():
    input_file = 'students.csv'
    output_file = 'graded_students.csv'
    processor = StudentProcessor(input_file)
    processor.read_students()
    avg_score = processor.calculate_average()
    processor.grade_students(avg_score)
    processor.write_results(output_file)
    print(f"Grading completed. Results written to {output_file}")

if __name__ == "__main__":
    main()

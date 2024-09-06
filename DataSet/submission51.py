import pandas as pd

def read_student_data(file_path):
    df = pd.read_csv(file_path)
    return df

def calculate_average(df):
    average_score = df['Score'].mean()
    return average_score

def assign_grade(df, average_score):
    df['Grade'] = df['Score'].apply(lambda x: 'A' if x >= average_score else 'B')
    return df

def write_results(df, output_file):
    df.to_csv(output_file, index=False)

def main():
    input_file = 'students.csv'
    output_file = 'graded_students.csv'
    student_df = read_student_data(input_file)
    avg_score = calculate_average(student_df)
    graded_df = assign_grade(student_df, avg_score)
    write_results(graded_df, output_file)
    print(f"Grades assigned and saved to {output_file}")

if __name__ == "__main__":
    main()

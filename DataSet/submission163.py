class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def show_faculties(self):
        print(f"Faculties in {self.college_name}:")
        for faculty in self.faculties:
            print(f"-- {faculty}")


def execute():
    college = College("Stanford College")
    college.add_faculty("Computer Engineering")
    college.add_faculty("Biology")
    college.add_faculty("History")

    college.show_faculties()


if __name__ == "__main__":
    execute()

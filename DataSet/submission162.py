class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def list_departments(self):
        print(f"Departments in {self.name}:")
        for dept in self.departments:
            print(f"- {dept}")


def main():
    uni = University("Harvard University")
    uni.add_department("Computer Science")
    uni.add_department("Mathematics")
    uni.add_department("Physics")

    uni.list_departments()


if __name__ == "__main__":
    main()

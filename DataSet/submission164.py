class Institution:
    def __init__(self, institution_name):
        self.institution_name = institution_name
        self.schools = []

    def add_school(self, school):
        self.schools.append(school)

    def display_schools(self):
        print(f"Schools under {self.institution_name}:")
        for school in self.schools:
            print(f"- {school}")


def run_system():
    inst = Institution("Oxford Institution")
    inst.add_school("Information Technology")
    inst.add_school("Law")
    inst.add_school("Chemistry")

    inst.display_schools()


if __name__ == "__main__":
    run_system()

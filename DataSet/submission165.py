class Academy:
    def __init__(self, academy_name):
        self.academy_name = academy_name
        self.programs = []

    def add_program(self, program):
        self.programs.append(program)

    def list_programs(self):
        print(f"Programs available at {self.academy_name}:")
        for program in self.programs:
            print(f"- {program}")


def manage_academy():
    academy = Academy("MIT Academy")
    academy.add_program("Electrical Engineering")
    academy.add_program("Philosophy")
    academy.add_program("Political Science")

    academy.list_programs()


if __name__ == "__main__":
    manage_academy()

class Person:
    def __init__(self, full_name, age, illness):
        # Initialize a person with full name, age, and illness
        self.full_name = full_name
        self.age = age
        self.illness = illness

    def display_details(self):
        # Show details of the person
        print(f"Full Name: {self.full_name}, Age: {self.age}, Illness: {self.illness}")

def register_patient(patient_list, full_name, age, illness):
    # Register a new patient in the system
    person = Person(full_name, age, illness)
    patient_list.append(person)

def view_patients(patient_list):
    # View all patients in the system
    for person in patient_list:
        person.display_details()

def run_hospital():
    # Manage hospital system
    patient_list = []
    register_patient(patient_list, "Alice Brown", 50, "Headache")
    register_patient(patient_list, "Bob Johnson", 62, "Fever")

    print("Registered patients in the hospital:")
    view_patients(patient_list)

if __name__ == "__main__":
    run_hospital()

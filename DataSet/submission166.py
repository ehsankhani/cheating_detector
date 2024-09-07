class Patient:
    def __init__(self, name, age, ailment):
        # Initialize patient with name, age, and ailment
        self.name = name
        self.age = age
        self.ailment = ailment

    def show_info(self):
        # Display patient information
        print(f"Patient Name: {self.name}, Age: {self.age}, Ailment: {self.ailment}")

def add_patient(patients, name, age, ailment):
    # Add a new patient to the list
    patient = Patient(name, age, ailment)
    patients.append(patient)

def list_patients(patients):
    # List all patients
    for patient in patients:
        patient.show_info()

def main():
    # Manage hospital patients
    patients = []
    add_patient(patients, "John Doe", 45, "Flu")
    add_patient(patients, "Jane Smith", 30, "Cold")

    print("Patients currently in the hospital:")
    list_patients(patients)

if __name__ == "__main__":
    main()

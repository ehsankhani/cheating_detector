class Inpatient:
    def __init__(self, patient_name, years_old, diagnosis):
        # Set up inpatient details
        self.patient_name = patient_name
        self.years_old = years_old
        self.diagnosis = diagnosis

    def print_info(self):
        # Output inpatient's info
        print(f"Name: {self.patient_name}, Age: {self.years_old}, Diagnosis: {self.diagnosis}")

def admit_patient(hospital_records, patient_name, years_old, diagnosis):
    # Admit a new patient to the hospital
    new_patient = Inpatient(patient_name, years_old, diagnosis)
    hospital_records.append(new_patient)

def show_patients(hospital_records):
    # Display all admitted patients
    for new_patient in hospital_records:
        new_patient.print_info()

def hospital_operations():
    # Handle hospital admission and viewing operations
    hospital_records = []
    admit_patient(hospital_records, "Chris Lee", 55, "Pneumonia")
    admit_patient(hospital_records, "Dana White", 38, "Asthma")

    print("Patients admitted to the hospital:")
    show_patients(hospital_records)

if __name__ == "__main__":
    hospital_operations()

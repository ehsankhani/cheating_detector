class HospitalEntry:
    def __init__(self, patient_full_name, patient_age, condition):
        # Initialize hospital entry for patient
        self.patient_full_name = patient_full_name
        self.patient_age = patient_age
        self.condition = condition

    def view_entry(self):
        # View patient entry details
        print(f"Name: {self.patient_full_name}, Age: {self.patient_age}, Condition: {self.condition}")

def enroll_patient(records, patient_full_name, patient_age, condition):
    # Enroll a new patient into hospital records
    entry = HospitalEntry(patient_full_name, patient_age, condition)
    records.append(entry)

def display_patients(records):
    # Display all hospital entries
    for entry in records:
        entry.view_entry()

def hospital_management():
    # Manage hospital admissions
    records = []
    enroll_patient(records, "Emily Clark", 40, "Allergies")
    enroll_patient(records, "Frank Wells", 60, "Back Pain")

    print("Patients listed in the hospital:")
    display_patients(records)

if __name__ == "__main__":
    hospital_management()

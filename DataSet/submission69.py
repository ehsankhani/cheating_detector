class Hospital:
    def __init__(self):
        self.patients = {}
        self.appointments = {}

    def add_patient(self, patient_id, name, age, ailment):
        self.patients[patient_id] = {"Name": name, "Age": age, "Ailment": ailment}

    def schedule_appointment(self, appointment_id, patient_id, doctor, date):
        if patient_id in self.patients:
            self.appointments[appointment_id] = {
                "Patient": self.patients[patient_id]["Name"],
                "Doctor": doctor,
                "Date": date
            }
        else:
            print(f"No patient found with ID {patient_id}")

    def list_patients(self):
        for patient_id, info in self.patients.items():
            print(f"ID: {patient_id}, Name: {info['Name']}, Age: {info['Age']}, Ailment: {info['Ailment']}")

    def list_appointments(self):
        for appointment_id, info in self.appointments.items():
            print(f"Appointment ID: {appointment_id}, Patient: {info['Patient']}, Doctor: {info['Doctor']}, Date: {info['Date']}")

def main():
    hospital = Hospital()

    hospital.add_patient(1, "Mark Spencer", 40, "Back Pain")
    hospital.add_patient(2, "Lucy Hale", 35, "Allergy")

    hospital.schedule_appointment(1, 1, "Dr. Green", "2024-09-20")
    hospital.schedule_appointment(2, 2, "Dr. White", "2024-09-21")

    print("Patient List:")
    hospital.list_patients()

    print("\nAppointment List:")
    hospital.list_appointments()

if __name__ == "__main__":
    main()

class Patient:
    def __init__(self, patient_id, name, age, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailment = ailment

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def list_patients(self):
        for patient in self.patients:
            print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Ailment: {patient.ailment}")

    def list_appointments(self):
        for appointment in self.appointments:
            print(f"Appointment ID: {appointment.appointment_id}, Patient: {appointment.patient.name}, Doctor: {appointment.doctor}, Date: {appointment.date}")

def main():
    hospital_system = HospitalManagementSystem()

    patient1 = Patient(1, "John Doe", 45, "Flu")
    patient2 = Patient(2, "Jane Smith", 30, "Cough")

    hospital_system.add_patient(patient1)
    hospital_system.add_patient(patient2)

    appointment1 = Appointment(1, patient1, "Dr. Alice", "2024-09-15")
    appointment2 = Appointment(2, patient2, "Dr. Bob", "2024-09-16")

    hospital_system.schedule_appointment(appointment1)
    hospital_system.schedule_appointment(appointment2)

    print("Patient List:")
    hospital_system.list_patients()

    print("\nAppointment List:")
    hospital_system.list_appointments()

if __name__ == "__main__":
    main()

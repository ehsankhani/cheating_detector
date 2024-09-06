class PatientInfo:
    def __init__(self, id, full_name, years, condition):
        self.id = id
        self.full_name = full_name
        self.years = years
        self.condition = condition

class AppointmentDetails:
    def __init__(self, id, patient, doctor, date):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.date = date

class Billing:
    def __init__(self, bill_id, patient, amount):
        self.bill_id = bill_id
        self.patient = patient
        self.amount = amount

class HospitalSystem:
    def __init__(self):
        self.patient_records = []
        self.appointments = []
        self.bills = []

    def register_patient(self, patient):
        self.patient_records.append(patient)

    def create_appointment(self, appointment):
        self.appointments.append(appointment)

    def generate_bill(self, bill):
        self.bills.append(bill)

    def show_patients(self):
        for patient in self.patient_records:
            print(f"ID: {patient.id}, Name: {patient.full_name}, Age: {patient.years}, Condition: {patient.condition}")

    def show_appointments(self):
        for appointment in self.appointments:
            print(f"Appointment ID: {appointment.id}, Patient: {appointment.patient.full_name}, Doctor: {appointment.doctor}, Date: {appointment.date}")

    def show_bills(self):
        for bill in self.bills:
            print(f"Bill ID: {bill.bill_id}, Patient: {bill.patient.full_name}, Amount: ${bill.amount}")

def main():
    system = HospitalSystem()

    patient_a = PatientInfo(101, "Alice Green", 29, "Headache")
    patient_b = PatientInfo(102, "Bob Brown", 54, "Fever")

    system.register_patient(patient_a)
    system.register_patient(patient_b)

    appointment_a = AppointmentDetails(1001, patient_a, "Dr. Martin", "2024-09-17")
    appointment_b = AppointmentDetails(1002, patient_b, "Dr. Lisa", "2024-09-18")

    system.create_appointment(appointment_a)
    system.create_appointment(appointment_b)

    bill_a = Billing(1, patient_a, 150.0)
    bill_b = Billing(2, patient_b, 200.0)

    system.generate_bill(bill_a)
    system.generate_bill(bill_b)

    print("Patient Records:")
    system.show_patients()

    print("\nAppointment Records:")
    system.show_appointments()

    print("\nBilling Records:")
    system.show_bills()

if __name__ == "__main__":
    main()

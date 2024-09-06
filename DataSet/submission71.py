class Staff:
    def __init__(self, staff_id, name, role):
        self.staff_id = staff_id
        self.name = name
        self.role = role

class Patient:
    def __init__(self, patient_id, name, age, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailment = ailment

class Billing:
    def __init__(self, bill_id, patient, amount, due_date):
        self.bill_id = bill_id
        self.patient = patient
        self.amount = amount
        self.due_date = due_date

class Hospital:
    def __init__(self):
        self.staff_members = []
        self.patients = []
        self.bills = []

    def add_staff(self, staff):
        self.staff_members.append(staff)

    def add_patient(self, patient):
        self.patients.append(patient)

    def create_bill(self, bill):
        self.bills.append(bill)

    def list_staff(self):
        for staff in self.staff_members:
            print(f"ID: {staff.staff_id}, Name: {staff.name}, Role: {staff.role}")

    def list_patients(self):
        for patient in self.patients:
            print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Ailment: {patient.ailment}")

    def list_bills(self):
        for bill in self.bills:
            print(f"Bill ID: {bill.bill_id}, Patient: {bill.patient.name}, Amount: ${bill.amount}, Due Date: {bill.due_date}")

def main():
    hospital = Hospital()

    staff1 = Staff(1, "Dr. Smith", "Cardiologist")
    staff2 = Staff(2, "Nurse Jane", "Nurse")

    hospital.add_staff(staff1)
    hospital.add_staff(staff2)

    patient1 = Patient(1, "Emma Watson", 30, "High Blood Pressure")
    patient2 = Patient(2, "Chris Evans", 40, "Diabetes")

    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    bill1 = Billing(1, patient1, 500.0, "2024-10-05")
    bill2 = Billing(2, patient2, 800.0, "2024-10-10")

    hospital.create_bill(bill1)
    hospital.create_bill(bill2)

    print("Staff List:")
    hospital.list_staff()

    print("\nPatient List:")
    hospital.list_patients()

    print("\nBilling List:")
    hospital.list_bills()

if __name__ == "__main__":
    main()

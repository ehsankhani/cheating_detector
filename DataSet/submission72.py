patients = {}
appointments = {}
staff = {}
bills = {}

def add_patient(patient_id, name, age, ailment):
    patients[patient_id] = {"Name": name, "Age": age, "Ailment": ailment}

def schedule_appointment(appointment_id, patient_id, doctor, date):
    if patient_id in patients:
        appointments[appointment_id] = {
            "Patient": patients[patient_id]["Name"],
            "Doctor": doctor,
            "Date": date
        }

def add_staff(staff_id, name, role):
    staff[staff_id] = {"Name": name, "Role": role}

def generate_bill(bill_id, patient_id, amount, due_date):
    if patient_id in patients:
        bills[bill_id] = {
            "Patient": patients[patient_id]["Name"],
            "Amount": amount,
            "Due Date": due_date
        }

def list_patients():
    for patient_id, info in patients.items():
        print(f"ID: {patient_id}, Name: {info['Name']}, Age: {info['Age']}, Ailment: {info['Ailment']}")

def list_appointments():
    for appointment_id, info in appointments.items():
        print(f"Appointment ID: {appointment_id}, Patient: {info['Patient']}, Doctor: {info['Doctor']}, Date: {info['Date']}")

def list_staff():
    for staff_id, info in staff.items():
        print(f"ID: {staff_id}, Name: {info['Name']}, Role: {info['Role']}")

def list_bills():
    for bill_id, info in bills.items():
        print(f"Bill ID: {bill_id}, Patient: {info['Patient']}, Amount: ${info['Amount']}, Due Date: {info['Due Date']}")

def main():
    add_patient(1, "Robert Downey", 55, "Arthritis")
    add_patient(2, "Scarlett Johansson", 35, "Asthma")

    schedule_appointment(1, 1, "Dr. Strange", "2024-10-15")
    schedule_appointment(2, 2, "Dr. Banner", "2024-10-20")

    add_staff(1, "Tony Stark", "Chief Surgeon")
    add_staff(2, "Natasha Romanoff", "Head Nurse")

    generate_bill(1, 1, 1000.0, "2024-10-25")
    generate_bill(2, 2, 1500.0, "2024-10-30")

    print("Patients:")
    list_patients()

    print("\nAppointments:")
    list_appointments()

    print("\nStaff:")
    list_staff()

    print("\nBills:")
    list_bills()

if __name__ == "__main__":
    main()

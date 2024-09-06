def add_patient(patients, patient_id, name, age, ailment):
    patients.append({"ID": patient_id, "Name": name, "Age": age, "Ailment": ailment})

def schedule_appointment(appointments, appointment_id, patient, doctor, date):
    appointments.append({"AppointmentID": appointment_id, "Patient": patient, "Doctor": doctor, "Date": date})

def list_patients(patients):
    for patient in patients:
        print(f"ID: {patient['ID']}, Name: {patient['Name']}, Age: {patient['Age']}, Ailment: {patient['Ailment']}")

def list_appointments(appointments):
    for appointment in appointments:
        print(f"Appointment ID: {appointment['AppointmentID']}, Patient: {appointment['Patient']['Name']}, Doctor: {appointment['Doctor']}, Date: {appointment['Date']}")

def main():
    patients = []
    appointments = []

    add_patient(patients, 1, "George Clooney", 50, "Vision Problems")
    add_patient(patients, 2, "Brad Pitt", 45, "Migraine")

    schedule_appointment(appointments, 1, patients[0], "Dr. Johnson", "2024-09-30")
    schedule_appointment(appointments, 2, patients[1], "Dr. Williams", "2024-10-01")

    print("Patients:")
    list_patients(patients)

    print("\nAppointments:")
    list_appointments(appointments)

if __name__ == "__main__":
    main()

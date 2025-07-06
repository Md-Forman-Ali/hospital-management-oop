class Patient:
    def __init__(self, id, name, age, gender, disease):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
    
    def show_it(self):
        print(f"ID : {self.id}")
        print(f"Patient Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Disease : {self.disease}")

class Doctor:
    def __init__(self, id, name, specialization, available_times):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.available_times = available_times

    def show_doctor(self):
        print(f"Doctor ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print("Available Times:")
        for time in self.available_times:
            print(f" - {time}")

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient    
        self.doctor = doctor      
        self.date = date
        self.time = time

    def show_info(self):
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Patient: {self.patient.name}")
        print(f"Doctor: {self.doctor.name} ({self.doctor.specialization})")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
    
    def add_patient(self):
        id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Gender: ")
        disease = input("Enter Disease Name: ")
        new_patient = Patient(id, name, age, gender, disease)
        self.patients.append(new_patient)
        print("Patient Added Successfully.")

    def remove_patient(self, id):
        for patient in self.patients:
            if patient.id == id:
                self.patients.remove(patient)
                print("Patient Removed Successfully.")
                return
        print("Patient Not Found.")

    def add_doctor(self):
        id = int(input("Enter Doctor ID: "))
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Doctor Specialization: ")
        available_times = input("Enter Available Times (comma separated): ").split(',')
        available_times = [time.strip() for time in available_times]
        new_doctor = Doctor(id, name, specialization, available_times)
        self.doctors.append(new_doctor)
        print("Doctor Added Successfully.")
    
    def remove_doctor(self, id):
        for doctor in self.doctors:
            if doctor.id == id:
                self.doctors.remove(doctor)
                print("Doctor Removed Successfully.")
                return
        print("Doctor Not Found.")
    
    def schedule_appointment(self):
        appointment_id = int(input("Enter Appointment ID: "))
        patient_id = int(input("Enter Patient ID: "))
        doctor_id = int(input("Enter Doctor ID: "))
        date = input("Enter Appointment Date: ")
        time = input("Enter Appointment Time: ")
        
        patient = None
        doctor = None

        for p in self.patients:
            if p.id == patient_id:
                patient = p
                break

        for d in self.doctors:
            if d.id == doctor_id:
                doctor = d
                break
        
        if patient and doctor:
            new_appointment = Appointment(appointment_id, patient, doctor, date, time)
            self.appointments.append(new_appointment)
            print("Appointment Scheduled Successfully.")
        else:
            print("Patient or Doctor Not Found.")

    def cancel_appointment(self, appointment_id):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                self.appointments.remove(appointment)
                print("Appointment Cancelled Successfully.")
                return
        print("Appointment Not Found.")

    def show_all_doctors(self):
        if not self.doctors:
            print("No Doctors Available.")
        else:
            for doctor in self.doctors:
                print("----------------------------")
                doctor.show_doctor()

    def show_all_patients(self):
        if not self.patients:
            print("No Patients Found.")
        else:
            for patient in self.patients:
                print("----------------------------")
                patient.show_it()

    def show_all_appointments(self):
        if not self.appointments:
            print("No Appointments Scheduled.")
        else:
            for appointment in self.appointments:
                print("----------------------------")
                appointment.show_info()


hospital = Hospital()

while True:
    print("\n--- Hospital Management System ---")
    print("1. Add Patient")
    print("2. Remove Patient")
    print("3. Add Doctor")
    print("4. Remove Doctor")
    print("5. Schedule Appointment")
    print("6. Cancel Appointment")
    print("7. Show All Patients")
    print("8. Show All Doctors")
    print("9. Show All Appointments")
    print("10. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        hospital.add_patient()
    elif choice == 2:
        id = int(input("Enter Patient ID to remove: "))
        hospital.remove_patient(id)
    elif choice == 3:
        hospital.add_doctor()
    elif choice == 4:
        id = int(input("Enter Doctor ID to remove: "))
        hospital.remove_doctor(id)
    elif choice == 5:
        hospital.schedule_appointment()
    elif choice == 6:
        id = int(input("Enter Appointment ID to cancel: "))
        hospital.cancel_appointment(id)
    elif choice == 7:
        hospital.show_all_patients()
    elif choice == 8:
        hospital.show_all_doctors()
    elif choice == 9:
        hospital.show_all_appointments()
    elif choice == 10:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Enter a valid choice (1-10).")

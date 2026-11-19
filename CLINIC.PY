
class Patient:
    
    clinic_name = "City Health Clinic"

    def __init__(self, patient_id, full_name, age, reason_for_visit):


        
        self.patient_id = patient_id
        self.full_name = full_name
        self.age = age
        self.reason_for_visit = reason_for_visit

    
    def display_patient(self):
        print("\n------ PATIENT RECORD ------")
        print("Clinic:", Patient.clinic_name)
        print("Patient ID:", self.patient_id)
        print("Full Name:", self.full_name)
        print("Age:", self.age)
        print("Reason for Visit:", self.reason_for_visit)
        print("Age Group:", self.age_group())

    
    def update_reason(self, new_reason):
        self.reason_for_visit = new_reason
        print(f"Reason updated for {self.full_name}.")

    
    def age_group(self):
        if self.age < 18:
            return "child"
        elif self.age < 60:
            return "adult"
        else:
            return "senior"



class ClinicQueue:

    def __init__(self):
        self.waiting_queue = []

    
    def add_patient(self, patient):
        self.waiting_queue.append(patient)
        print(f"{patient.full_name} added to the queue.")

    
    def display_queue(self):
        print("\n------ CLINIC WAITING QUEUE ------")

        if not self.waiting_queue:
            print("The waiting queue is empty.")
        else:
            for position, patient in enumerate(self.waiting_queue, start=1):
                print(
                    f"{position}. {patient.full_name} "
                    f"(ID: {patient.patient_id})"
                )

    
    def serve_next_patient(self):
        if not self.waiting_queue:
            print("No patients to serve. Queue is empty.")
        else:
            patient = self.waiting_queue.pop(0)
            print(f"Now serving: {patient.full_name}")

patient1 = Patient(101, "John Kamau", 12, "Fever")
patient2 = Patient(102, "Mary Wanjiku", 25, "Headache")
patient3 = Patient(103, "Peter Otieno", 65, "Joint pain")
patient4 = Patient(104, "Grace Achieng", 35, "Stomach pain")
patient5 = Patient(105, "David Mwangi", 17, "Cough")




patients = [patient1, patient2, patient3, patient4, patient5]

for patient in patients:
    patient.display_patient()




print("\n------ UPDATE PATIENT REASON ------")

patient2.update_reason("Migraine")

patient2.display_patient()

print("\nChecking another patient:")
patient1.display_patient()




clinic_queue = ClinicQueue()


clinic_queue.display_queue()
clinic_queue.serve_next_patient()


print("\nAdding patients to the queue:")

clinic_queue.add_patient(patient1)
clinic_queue.add_patient(patient2)
clinic_queue.add_patient(patient3)
clinic_queue.add_patient(patient4)
clinic_queue.add_patient(patient5)


clinic_queue.display_queue()



clinic_queue.serve_next_patient()
clinic_queue.serve_next_patient()

# Display remaining queue
clinic_queue.display_queue()

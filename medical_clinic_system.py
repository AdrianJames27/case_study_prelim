from patient import Patient

class MedicalClinicSystem:
    def __init__(self):
        self._patients = {}

    @property
    def patients(self):
        return self._patients
    
    def init_system(self):
        while True:
            print("\n--- SOAP Medical Clinic System ---")
            print("Enter a number to proceed")
            print("[1] Add New Patient and SOAP Note")
            print("[2] Update Existing Patient Info")
            print("[3] Update Existing SOAP Note")
            print("[4] View Patient SOAP Note")
            print("[5] Exit")
            choice = input("Select an option: ")

            match choice:
                case '1':
                    add_patient_and_note()
                case '2':
                    if len(self.patients) == 0:
                        print("No patient is added yet.")
                    else:
                        update_patient_info()
                case '3':
                    if len(self.patients) == 0:
                        print("No patient is added yet.")
                    else:
                        update_note()
                case '4':
                    if len(self.patients) == 0:
                        print("No patient is added yet.")
                    else:
                        view_patient_note()
                case '5':
                    print("Exiting the system.")

                    # stop loop
                    break
                case _:
                    print("Invalid choice. Please try again.")
        
        def display_patients():
            print("----- List of Patient/s -----")
            for patient in self.patients.values():
                print(f"ID : {patient.patient_id:0>5}, Name: {patient.name}")
            print("-----------------------------")
        
        def add_patient_and_note():
            name = ''
            age = 0
            contact = ''

            while True:
                name = input("Enter Patient Name: ")

                if name.isdigit():
                    print("Name cannot be a number.")
                elif name.strip() == "":
                    print("Name cannot be empty.")
                else:
                    # stop loop
                    break

            while True:
                try:
                    age = int(input("Enter Patient Age: "))

                    if age < 0:
                        print("Age cannot be lower than 0.")
                    else:
                        # stop loop
                        break
                except ValueError:
                    print("Enter only a number.")
            
            contact = input("Enter Contact Info: ")

            if contact.strip() == "":
                contact = "No contact number"

            patient = Patient(name, age, contact)

            print("\nEnter Subjective Data:")
            patient.soap_note.subjective.input_data()

            print("\nEnter Objective Data:")
            patient.soap_note.objective.input_data()

            print("\nAnalyzing data for Assessment...")
            patient.soap_note.assessment.analyze(patient.soap_note.subjective, patient.soap_note.objective)

            print("\nEnter Plan:")
            patient.soap_note.plan.update_plan()

            self.patients.update({ patient.patient_id: patient })

            print("\nPatient SOAP Note created successfully.")
        
        def update_patient_info():
            while True:
                try:
                    display_patients()

                    pid = int(input("Enter Patient ID to update: "))

                    if pid in self.patients:
                        patient = self.patients[pid]

                        name = ''
                        age = 0
                        contact = ''

                        while True:
                            name = input("Enter Patient Name: ", )

                            if name.isdigit():
                                print("Name cannot be a number.")
                            elif name.strip() == "":
                                print("Name cannot be empty.")
                            else:
                                # stop loop
                                break

                        while True:
                            try:
                                age = int(input("Enter Patient Age: "))

                                if age < 0:
                                    print("Age cannot be lower than 0.")
                                else:
                                    # stop loop
                                    break
                            except ValueError:
                                print("Enter only a number.")
                        
                        contact = input("Enter Contact Info: ")

                        if contact.strip() == "":
                            contact = "No contact number"

                        # update patient info
                        patient.name = name
                        patient.age = age
                        patient.contact = contact

                        print("\nPatient Info successfully updated.")
                    else:
                        print("Patient not found.")
                    
                    # stop loop
                    break
                except ValueError:
                    print("Enter only number.")
        
        def update_note():
            while True:
                try:
                    display_patients()

                    pid = int(input("Enter Patient ID to update: "))
            
                    if pid in self.patients:
                        patient = self.patients[pid]

                        patient.soap_note.display_note()

                        while True:
                            print("\nWhich section would you like to update? (subjective/objective/assessment/plan)")
                            print("(Type 'q' to quit)")
                            section = input("Section: ")

                            if section.isdigit():
                                print("Pick only one of the four section")
                            elif section in ['subjective', 'objective', 'assessment', 'plan']:
                                match section:
                                    case 'subjective':
                                        patient.soap_note.subjective.input_data()
                                    case 'objective':
                                        patient.soap_note.objective.input_data()
                                    case 'plan':
                                        patient.soap_note.plan.update_plan()
                                    case 'assessment':
                                        patient.soap_note.assessment.analyze(patient.soap_note.subjective, patient.soap_note.objective)
                                        print("\nAssessment updated based on the latest data.")

                                print(f"\n{section.capitalize()} updated successfully.")

                                # stop loop
                                break
                            elif section.lower() == 'q':
                                print("Operation cancelled.")

                                # stop loop
                                break
                            else:
                                print("Invalid section choice.")
                    else:
                        print("Patient not found.")

                    # stop loop
                    break
                except ValueError:
                    print("Enter only number.")
        
        def view_patient_note():
            while True:
                display_patients()

                try:
                    pid = int(input("Enter Patient ID to view: "))

                    if pid in self.patients:
                        patient = self.patients[pid]

                        patient.display_info()
                        patient.soap_note.display_note()
                    else:
                        print("Patient not found.")
                    
                    # stop loop
                    break
                except ValueError:
                    print("Enter only number.")
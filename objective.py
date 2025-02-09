class Objective:
    def __init__(self):
        self._vital_signs = {}
        self._lab_results = {}
        self._physical_exam = ""

    @property
    def vital_signs(self):
        return self._vital_signs
    
    @property
    def lab_results(self):
        return self._lab_results
    
    @property
    def physical_exam(self):
        return self._physical_exam
    
    @vital_signs.setter
    def vital_signs(self, new_vital_signs):
        self._vital_signs = new_vital_signs
    
    @lab_results.setter
    def lab_results(self, new_lab_results):
        self._lab_results = new_lab_results
    
    @physical_exam.setter
    def physical_exam(self, new_physical_exam):
        self._physical_exam = new_physical_exam

    def input_data(self):
        """
        Updates the objective data for a patient.
        """

        bp = input("Enter blood pressure (format: systolic/diastolic, e.g., 120/80): ")
        hr = 0
        
        while True:
            try:
                hr = int(input("Enter heart rate Beats Per Minute (BPM): "))

                # stop loop
                break
            except ValueError:
                print("Enter only number.")

        self.vital_signs.update({ 'Blood Pressure': bp, 'Heart Rate': hr })

        self.physical_exam = input("Enter physical exam notes: ")

        # Loop to allow entry of multiple lab results
        lab_results = {}
        
        while True:
            add_lab = input("Do you want to enter a lab result? (yes/no): ").strip().lower()
            if add_lab in ['yes', 'y']:
                lab_name = input("Enter lab test name (e.g., CBC): ")
                lab_value = input(f"Enter result for {lab_name}: ")
                lab_results.update({ lab_name: lab_value })
            elif add_lab in ['no', 'n']:
                # stop loop
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")

        self.lab_results = lab_results

    def display(self):
        print("\nObjective Data:")
        print("Vital Signs:")
        for k, v in self.vital_signs.items():
            print(f"  {k:5}: {v}")
        print("Lab Results:")
        for k, v in self.lab_results.items():
            print(f"  {k:5}: {v}")
        print(f"Physical Exam: {self.physical_exam}")
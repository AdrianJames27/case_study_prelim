class Subjective:
    def __init__(self):
        self.medical_history = ""
        self.current_symptoms = ""
        self.concerns = ""

    def input_data(self):
        """
        Updates the subjective data for a patient.
        """

        self.medical_history = input("Enter medical history: ")
        self.current_symptoms = input("Enter current symptoms: ")
        self.concerns = input("Enter patient concerns: ")

    def display(self):
        print("\nSubjective Data:")
        print(f"History     : {self.medical_history}")
        print(f"Symptoms    : {self.current_symptoms}")
        print(f"Concerns    : {self.concerns}")
class Subjective:
    def __init__(self):
        self._medical_history = ""
        self._current_symptoms = ""
        self._concerns = ""

    @property
    def medical_history(self):
        return self._medical_history

    @property
    def current_symptoms(self):
        return self._current_symptoms

    @property
    def concerns(self):
        return self._concerns

    @medical_history.setter
    def medical_history(self, new_medical_history):
        self._medical_history = new_medical_history

    @current_symptoms.setter
    def current_symptoms(self, new_current_symptoms):
        self._current_symptoms = new_current_symptoms

    @concerns.setter
    def concerns(self, new_concerns):
        self._concerns = new_concerns

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
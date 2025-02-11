class Assessment:
    def __init__(self):
        self._diagnosis = ""
        self._differential_diagnoses = []
        self._clinical_notes = ""

    @property
    def diagnosis(self):
        return self._diagnosis
    
    @property
    def differential_diagnoses(self):
        return self._differential_diagnoses
    
    @property
    def clinical_notes(self):
        return self._clinical_notes
    
    @diagnosis.setter
    def diagnosis(self, new_diagnosis):
        self._diagnosis = new_diagnosis
    
    @differential_diagnoses.setter
    def differential_diagnoses(self, new_differential_diagnoses):
        self._differential_diagnoses = new_differential_diagnoses
    
    @clinical_notes.setter
    def clinical_notes(self, clinical_notes):
        self._clinical_notes = clinical_notes

    def analyze(self, subjective, objective):
        """
        Analyzes the subjective and objective data to determine a primary diagnosis,
        possible differential diagnoses, and clinical notes.
        """
        
        # Convert inputs to lowercase for consistent comparisons.
        symptoms = subjective.current_symptoms.lower()
        exam_notes = objective.physical_exam.lower() if objective.physical_exam else ""
        
        # Initialize a list to store possible diagnoses.
        possible_diagnoses = []
        
        # Analyze subjective symptoms.
        if "fever" in symptoms:
            # Look for additional respiratory symptoms.
            if "cough" in symptoms or "shortness of breath" in symptoms:
                possible_diagnoses.append("Respiratory infection (e.g., pneumonia)")
            else:
                possible_diagnoses.append("Infection")
        if "chest pain" in symptoms:
            possible_diagnoses.append("Cardiac issues")
        if "headache" in symptoms:
            possible_diagnoses.append("Migraine")
        
        # Analyze objective data: vital signs.
        bp = objective.vital_signs.get("Blood Pressure", "")
        if bp:
            try:
                # Expecting a format like '120/80'
                systolic = int(bp.split('/')[0])
                if systolic > 140:
                    possible_diagnoses.append("Hypertensive condition")
            except (ValueError, IndexError):
                pass  # Skip parsing errors.

        hr = objective.vital_signs.get("Heart Rate", 0)
        if hr:
            if hr < 60:
                possible_diagnoses.append("Sick Sinus Syndrome")
            elif hr > 100:
                possible_diagnoses.append("Atrial Fibrillation")
        
        temp = objective.vital_signs.get("Body Temperature", 0)
        if temp:
            try:
                temp = float(temp)
                if temp > 100.4:  # Fever threshold in Fahrenheit (or >38°C)
                    possible_diagnoses.append("Fever")
            except ValueError:
                pass  # Skip parsing errors
        
        # Analyze lab results (if any).
        for lab, result in objective.lab_results.items():
            if lab == "CBC" and "abnormal" in result.lower():
                possible_diagnoses.append("Possible hematologic disorder")
            elif lab == "BMP" and "abnormal" in result.lower():
                possible_diagnoses.append("Possible kidney dysfunction")
            elif lab == "LFT" and "abnormal" in result.lower():
                possible_diagnoses.append("Possible liver disease")
        
        # Analyze physical exam notes.
        if "inflamed" in exam_notes or "swollen" in exam_notes:
            possible_diagnoses.append("Signs of inflammation")
        
        # Set the primary diagnosis and differential diagnoses.
        if possible_diagnoses:
            self.diagnosis = possible_diagnoses[0]  # Primary diagnosis.
            self.differential_diagnoses = possible_diagnoses[1:]  # Remaining as differentials.
        else:
            self.diagnosis = "Undetermined"
            self.differential_diagnoses.clear()
        
        # Provide additional clinical notes based on findings.
        if "Signs of inflammation" in self.differential_diagnoses:
            self.clinical_notes = "Physical exam indicates inflammation; consider further imaging."
        else:
            self.clinical_notes = "Additional tests are recommended to confirm the diagnosis."


    def display(self):
        print("\nAssessment:")
        print(f"Diagnosis: {self.diagnosis}")
        if self.differential_diagnoses:
            print("Differential Diagnoses:")
            for diag in self.differential_diagnoses:
                print(f"  {diag}")
        print(f"Clinical Notes: {self.clinical_notes}")
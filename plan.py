class Plan:
    def __init__(self):
        self._treatment_plan = ""
        self._follow_up = ""
        self._additional_tests = ""

    @property
    def treatment_plan(self):
        return self._treatment_plan
    
    @property
    def follow_up(self):
        return self._follow_up
    
    @property
    def additional_tests(self):
        return self._additional_tests
    
    @treatment_plan.setter
    def treatment_plan(self, new_treatment_plan):
        self._treatment_plan = new_treatment_plan
    
    @follow_up.setter
    def follow_up(self, new_follow_up):
        self._follow_up = new_follow_up
    
    @additional_tests.setter
    def additional_tests(self, new_additional_tests):
        self._additional_tests = new_additional_tests

    def add_plan(self, assessment):
        """
        Generates a treatment plan, follow-up, and additional tests based on the diagnosis and clinical notes.
        """
        primary_diagnosis = assessment.diagnosis
        differentials = assessment.differential_diagnoses
        clinical_notes = assessment.clinical_notes

        if "infection" in primary_diagnosis.lower():
            self.treatment_plan = "Start antibiotics and monitor symptoms."
        elif "cardiac" in primary_diagnosis.lower():
            self.treatment_plan = "Refer to cardiology and start aspirin therapy if indicated."
        elif "migraine" in primary_diagnosis.lower():
            self.treatment_plan = "Prescribe pain relievers and recommend lifestyle changes."
        elif "hypertensive" in primary_diagnosis.lower():
            self.treatment_plan = "Initiate antihypertensive medication and lifestyle modification."
        else:
            self.treatment_plan = "Symptomatic treatment and further evaluation."
        

        if "undiagnosed" in primary_diagnosis.lower() or not differentials:
            self.follow_up = "Schedule a follow-up in 1 week to reassess symptoms."
        else:
            self.follow_up = "Follow-up in 2-4 weeks based on response to treatment."
        
        if "Signs of inflammation" in differentials or "further imaging" in clinical_notes.lower():
            self.additional_tests = "Order CBC, CRP, and imaging studies."
        elif "cardiac" in primary_diagnosis.lower():
            self.additional_tests = "Order ECG and cardiac enzyme tests."
        elif "kidney" in differentials:
            self.additional_tests = "Order renal function tests."
        elif "fever" in primary_diagnosis.lower():
            self.additional_tests = "Check WBC count, blood cultures, and inflammatory markers."
        else:
            self.additional_tests = "Consider additional lab tests based on clinical course."
        

    def update_plan(self):
        """
        Update the treatment plan details.
        """

        while True:
            print("\n--- Plan Update Menu ---")
            print("[1] Update Treatment Plan")
            print("[2] Update Follow-Up Details")
            print("[3] Update Additional Tests or Referrals")
            print("[4] Display Current Plan")
            print("[5] Finish Updating")
            choice = input("Select an option: ")

            match choice:
                case '1':
                    self.treatment_plan = input("Enter treatment plan details: ")
                    print("Treatment plan updated.")
                case '2':
                    self.follow_up = input("Enter follow-up details: ")
                    print("Follow-up details updated.")
                case '3':
                    self.additional_tests = input("Enter additional tests or referrals: ")
                    print("Additional tests/referrals updated.")
                case '4':
                    self.display()
                case '5':
                    print("Finished updating the plan.")
                    break
                case _:
                    print("Invalid option, please try again.")

    def display(self):
        print("\nPlan:")
        print(f"Treatment Plan              : {self.treatment_plan}")
        print(f"Follow-up                   : {self.follow_up}")
        print(f"Additional Tests/Referrals  : {self.additional_tests}")
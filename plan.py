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
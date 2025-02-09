from subjective import Subjective
from objective import Objective
from assessment import Assessment
from plan import Plan

class SOAPNote:
    def __init__(self):
        self._subjective = Subjective()
        self._objective = Objective()
        self._assessment = Assessment()
        self._plan = Plan()

    @property
    def subjective(self):
        return self._subjective
    
    @property
    def objective(self):
        return self._objective
    
    @property
    def assessment(self):
        return self._assessment
    
    @property
    def plan(self):
        return self._plan

    def display_note(self):
        print("\n--- SOAP Note ---")
        self.subjective.display()
        self.objective.display()
        self.assessment.display()
        self.plan.display()
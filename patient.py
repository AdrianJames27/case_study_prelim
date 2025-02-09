from soap_note import SOAPNote

class Patient:
    patient_id_counter = 1

    def __init__(self, name, age, contact_info):
        self._patient_id = Patient.patient_id_counter
        self._name = name
        self._age = age
        self._contact_info = contact_info
        self._soap_note = SOAPNote()  # Each patient gets a SOAP note

        Patient.patient_id_counter += 1

    @property
    def patient_id(self):
        return self._patient_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def contact_info(self):
        return self._contact_info
    
    @property
    def soap_note(self):
        return self._soap_note
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @age.setter
    def age(self, new_age):
        self._age = new_age
    
    @contact_info.setter
    def contact_info(self, new_contact_info):
        self._contact_info = new_contact_info

    def display_info(self):
        print(self)

    def __str__(self):
        return (
            f"Patient ID  : {self._patient_id}\n"
            f"Name        : {self._name}\n"
            f"Age         : {self._age}\n"
            f"Contact     : {self._contact_info}"
        )
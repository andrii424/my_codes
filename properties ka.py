class KgToPounds:

    def __init__(self, kilo):
        self._kilo = kilo

    def kg_to_pounds(self):
        return self._kilo * 2.6
    
    def get_kg(self):
        return self._kilo 
    
    def set_kg(self, kilo):
        if isinstance(kilo, (int, float)):
            self._kilo = kilo
        else:
            print("Please enter a valid number")

    

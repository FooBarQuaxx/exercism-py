
class Allergies(object):
    ALLERGIES = {
        'eggs': 1 << 0,
        'peanuts': 1 << 1,
        'shellfish': 1 << 2,
        'strawberries': 1 << 3,
        'tomatoes': 1 << 4,
        'chocolate': 1 << 5,
        'pollen': 1 << 6,
        'cats': 1 << 7,
    }

    def __init__(self, allergies):
        self.allergies = allergies

    def is_allergic_to(self, allergy):
        return self.ALLERGIES.get(allergy) & self.allergies

    @property
    def lst(self):
        return [allergy for allergy, code in self.ALLERGIES.items() if code & self.allergies]


class Calorie:
    # bmr= 10*weight + 6.5*height - 5*age + 5 - 10*temperature
    def __init__(self, weight, height, age, temperature):
        self.weight= weight
        self.height= height
        self.age= age
        self.temperature= temperature
    def calculate_calories(self):
        return 10*self.weight + 6.5*self.height - 5*self.age + 5 - 10*self.temperature
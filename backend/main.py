from temperature import Temperature
from calorie import Calorie

temp= Temperature(country="israel",city="jerusalem")
calorie= Calorie(weight=101.5, height=179, age=31, temperature=temp.get_temperature())
print(calorie.calculate_calories())
car = {"Brand": "Ford", "Model": "Mustang", "Year": 1964}
car.pop("Model")
print(car)

sports = {1: "soccer", 2: "baseball", 4:"swimming", 5:"basketball"}
l = len(sports)
index = l//2
print(sports[index])

print(3 in sports)
print(sports.pop(5))
sports[3] = "judo"
print(sports)
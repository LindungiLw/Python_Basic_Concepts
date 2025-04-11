country_code = {1: "US", 20: "Egypt", 30: "Greece", 39: "Italy", 81: "Japan", 82: "South Korea", 62: "Indonesia"}
print(len(country_code))
print(country_code[62])
print(country_code[82])

print(82 in country_code)
print(60 in country_code)
country_code[60] = "Malaysia"
print(60 in country_code)
country_code.pop(81)
print(81 in country_code)
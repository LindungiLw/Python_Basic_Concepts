city = {"New York City": 8175133, "Los Angeles": 3792621, "Washington": 632323, "Chicago": 2695598, "Toronto": 2615060, "Montreal": 11854442, "Ottawa": 883391, "Boston": 62600}
print(city["Toronto"])
print(city["Boston"])

food = {"ham" : "yes", "egg": "yes", "spam": "no"}
print(food)

food["spam"] = "yes"
print(food)

country = {"Indonesia": 1, "USA": 2, "Germany": 3, "France": 4, "Mexico": 8}
print(country["Indonesia"])
print(country["France"])
print(country["Mexico"])

print(country.pop("Germany"))
print(country.pop("France"))
print(country)
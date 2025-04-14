fruits = ['apple', 'banana', 'grape', 'mango', 'durian']
fruits_input = input("Enter your favorite fruit: ")

if fruits_input not in fruits:
    print("The fruit is not in the list.")
elif fruits_input == "durian":
    print("You are durian-lover!")
else:
    print("Try durian; you're sure to like it.")
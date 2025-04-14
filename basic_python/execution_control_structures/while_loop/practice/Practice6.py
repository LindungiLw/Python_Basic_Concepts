total_items = 0
total_amount = 0

amount = int(input("Enter the item price (<= 10000): "))

while amount <= 10000:
    total_items += 1
    total_amount += amount
    amount = int(input("Enter the item price (<= 10000): "))

print("Number of items to be purchased:", total_items)
print("Total amount:", total_amount, "Rupiah")

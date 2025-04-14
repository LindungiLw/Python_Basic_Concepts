amount = int(input("Enter your transaction amount: "))

if amount > 1000000:
    comm = amount * 0.5
elif amount > 500000:
    comm = amount * 0.7
elif amount > 200000:
    comm = amount * 1.0
else:
    comm = 15000

print("Transaction amount =", amount,"Commission =", comm)
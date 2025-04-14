balance = float(input("Enter initial account balance: "))

def deposit(money):
    global balance
    balance += money
    print("Deposited:", money)
    print("Current balance:", balance)

def withdraw(money):
    global balance
    if money <= balance:
        balance -= money
        print("Withdrawn:", money)
    else:
        print("Insufficient balance!")
    print("Current balance:", balance)

deposit_amount = float(input("Enter deposit amount: "))
withdraw_amount = float(input("Enter withdrawal amount: "))

deposit(deposit_amount)
withdraw(withdraw_amount)

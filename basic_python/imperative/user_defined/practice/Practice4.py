def lennum(n1):
    num_str = str(n1)
    num_digits = len(num_str)
    last_digit = int(num_str[-1])
    return num_digits, last_digit

n = int(input("Enter a positive integer: "))
digits, last = lennum(n)

print("Number of digits:", digits)
print("Last digit:", last)

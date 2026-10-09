a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def GCD(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

print("GCD of", a, "and", b, "is:", GCD(a, b))

def LCM(a, b):
    return (a * b) // GCD(a, b)

print("LCM of", a, "and", b, "is:", LCM(a, b))
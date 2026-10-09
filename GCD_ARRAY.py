arr = [12, 24, 26]

def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

result = arr[0]
for number in arr[1:]:
    result = gcd(result, number)
print("GCD of the array is:", result)
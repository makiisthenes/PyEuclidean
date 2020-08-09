# Euclidean Algorithm Python Implementation.

def gcd(r0, r1):
    if r0 < r1:
        inter = r0
        r0 = r1
        r1 = inter
    r = 1
    while r != 0:
        r = r0 % r1
        inter = r1
        if r != 0:
            r1 = r
        r0 = inter
    print(f"GCD of these 2 integers is: {r1}.")


# Main
print("Implementation of Euclidean Algorithm in Python.")
while True:
    int1 = int(input("Enter integer 1:: "))
    int2 = int(input("Enter integer 2:: "))
    gcd(int1, int2)

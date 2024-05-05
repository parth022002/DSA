def euclid_gcd(a, b):  # Define a function named euclid_gcd that takes two integers a and b as input.
    while b != 0:  # Start a while loop that continues as long as b is not equal to zero.
        a, b = b, a % b  # Swap the values of a and b, and update a to the remainder of the division of a by b.
    return a  # Return the value of a, which represents the greatest common divisor (GCD) of the original a and b.

# Test Case:
num1 = 48
num2 = 18
gcd = euclid_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)

# Simple program to demonstrate the use of the modulus operator (%)

# Input a number from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by 5
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    remainder = number % 5
    print(f"{number} is not divisible by 5. Remainder is {remainder}.")
    


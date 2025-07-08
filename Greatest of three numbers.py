# to find the greatest of three numbers
def find_greatest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else :
        return c
    
# Input from user
num1 = float (input("Enter the first number:"))
num2 = float (input("Enter the second number:"))
num3 = float (input("Enter the third number:"))

#Function call
greatest = find_greatest (num1, num2, num3)

# display the result
print(f"the greatest number is : {greatest}")

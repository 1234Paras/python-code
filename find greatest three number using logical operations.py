''' program that accepts three numbers from user and
prints the largest number using logical operator.'''

a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
print("You entered number is ",a,b,c)

if(a>=b and a>=c):
    print("Largest number is ",a)
    
if(b>=a and b>=c):
    print("Largest number is ",b)
    
if(c>=a and c>=b):
    print("Largest number is ",c)

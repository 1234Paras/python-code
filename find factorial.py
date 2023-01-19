'''program to find the factorial of a positive integer.'''

a=int(input("Enter a number"))

def printfactorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print("Factorial of ",a,"is ",fact)

printfactorial(a)

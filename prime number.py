'''program to print prime numbers between 1 to 100.'''

print("Enter a number",end=" ")
no=int(input())

def primeno_test(no):
    isprime=0
    for i in range(2,no):
        if(no%i==0):
            isprime=1
            break
    return isprime

def primeno_gen(no):
    isprime=0
    for i in range(2,no):
        if(primeno_test(i)==0):
            print(" ",i)

primeno_gen(no)
primeno_test(no)
    

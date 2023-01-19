#program to read two numbers from keyboard and swap these numbers.

temp=0
def swap_numbers():
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    print("Value before swap of a is : ",a)
    print("Value before swap of b is : ",b)
    temp=a
    a=b
    b=temp
    print("Values after swap of a : ",a)
    print("Values after swap of b : ",b)

swap_numbers()
          

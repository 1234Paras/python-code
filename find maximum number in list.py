'''Python program to find a maximum number in an list.'''

SIZE=10
list1=[]
def accept_number():
    for i in range(0,SIZE):
        no=int(input("Enter the elements is"))
        list1.append(no)

def max_number():
    maximum_number=max(list1)
    print("Maximum element is",maximum_number)
    
accept_number()
max_number()


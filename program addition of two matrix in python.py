'''program to add two n * m matrix.'''

SIZE=10
ROW=3
COL=3
list1=[]

def input_number():
    for i in range(0,ROW):
        no=[]
        for j in range(0,COL):
            no.append(int(input("Enter the element is")))
        list1.append(no)

def addition_matrix():
    for i in range(0,ROW):
        for j in range(0,COL):
            
            print(list1[i][j],end=" ")
        print()

input_number()
addition_matrix()

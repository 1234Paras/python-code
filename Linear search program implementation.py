'''python program to linear search.'''

l=[50,10,60,30,20,80]
x=int(input("Enter an element that you want to search"))
flag=False
for i in range(len(l)):
    if l[i]==x:
        print("Element found at",i,"index")
        flag=True
        break
if flag == False:
    print("Element not found ")

'''python Program to create Bubble sort.'''

arr=[]
j=0
def bubble_sort(arr):
    SIZE=len(arr)
    for i in range(0,SIZE):
        for j in range(0,SIZE-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print(*arr)

def input_number():
    n=int(input("Enter how many elements you want to store"))
    for i in range(0,n):
        item=int(input("Enter element"))
        arr.append(item)

input_number()
print("Array before bubble sort")
print(*arr)
bubble_sort(arr)
print("Array after bubble sort")
print(*arr)
    

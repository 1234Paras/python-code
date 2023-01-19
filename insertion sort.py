'''python Program to create Insertion sort.'''

arr=[]
def insertion_sort(arr):
    for i in range(0,10):
        j=i
        while (j>0 and arr[j]<arr[j-1]):
               arr[j],arr[j-1] = arr[j-1],arr[j]
               j = j-1
               print(*arr)
def input_number():
    n=int(input("Enter how many elements you want to store"))
    for i in range(0,n):
        item=int(input("Enter element"))
        arr.append(item)

input_number()
print("Array before insertion sort")
print(*arr)
insertion_sort(arr)
print("Array after insertion sort")
print(*arr)

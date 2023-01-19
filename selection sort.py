'''python Program to create Selection sort.'''

arr=[]
def selection_sort(arr):
    SIZE= len(arr)
    for i in range(0,SIZE):
        mid_index=i
        for j in range(i+1,SIZE):
            if arr[j]<arr[mid_index]:
                mid_index=j
                
        arr[i],arr[mid_index]=arr[mid_index],arr[i]
        print(*arr)
def input_number():
    n=int(input("Enter how many elements you want to store"))
    for i in range(0,n):
        item=int(input("Enter element"))
        arr.append(item)

input_number()
print("Array before selection sort")
print(*arr)
selection_sort(arr)
print("Array after selection sort")
print(*arr)

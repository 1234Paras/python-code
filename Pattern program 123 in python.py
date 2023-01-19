'''Pattern program
1 2 3
1 2 3
1 2 3
'''
ROW = 3
COL = 3
for i in range(1,ROW+1):
    for j in range(1,COL+1):
        print(j,end=" ")
    print("\r")

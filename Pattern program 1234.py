'''Patttern Program
1 2  3  4
5 6  7  8
9 10 11 12
'''
ROW=3
COL=4
k=1
for i in range(1,ROW+1):
    for j in range(1,COL+1):
        print(k,k+1,end='')
    print("\r")

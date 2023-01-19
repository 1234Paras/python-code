'''Pattern program
****
***
**
*
'''

ROW=4
for i in range(ROW+1,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")

#FOR CREATING DIAMOND:
for i in range(1,10):
    for j in range(10-i):
        print(end="  ")#for spacing
    for j in range(i*2):
        print("*",end=" ")
    print()  
for i in range(10,0,-1):
    for j in range(10-i):
        print(end="  ")
    for j in range(i*2):
        print("*",end=" ")
    print()
print("\n")
#CREATING X:
for i in range(1,15):
    for j in range(1,14):
        if i+j==14 or i==j  :
            print("*", end=" ")
        else:
            print(end="  ")
    print()
print("\n")
#CREATING z:
for i in range(10):
    for j in range(10):
        if i==0 or i==9 or i+j==9: #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()



     
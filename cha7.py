#chapter 7 while ,for loop
i=0
while i<=50:
    print("",i)
    i=i+1

for i in range(4):
    print("printing")
    if i % 2 == 0:
        continue
    print(i)
#CHAPTER 7 – PRACTICE SET 
#q1 table of 2
num=2
for i in range (1,11):
    print(f"{num} x {i}={num*i}")
print("end of example")
print("\n")
#q7 upper triangle 
for i in range(1,10):
    for j in range(9-i):
        print(end="  ")#for spacing
    for j in range(i*2):
        print("*",end=" ")
    print() 
print("\n")
#q8 left angle triangle
for i in range(1,7):
    for j in range(i):
        print("*",end=" ")
    print() 
print("\n")
#q9 8
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) or(i==0 or i==3)or (i==0 or i==6)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("\n")
# for 3
for i in range(7):
    for j in range(5):
        if ((j==4 or j==6) or(i==0 or i==3)or (i==0 or i==6)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("\n")
# for 2
for i in range(7):
    for j in range(5):
        if ((i>3 and j==0)or(i==0 or i==3 or i==6)or (i<3 and j==4)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#for 4
print("\n")
for i in range(7):
    for j in range(5):
        if ((i+j==4) or (j==4)or (i==4)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("\n")
# FOR CREATING 5
for i in range(7):
    for j in range(5):
        if ((i<3 and j==0)or(i==0 or i==3 or i==6)or (j==4 and i>3)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()

print("\n")
# FOR CREATING 6
for i in range(7):
    for j in range(5):
        if (( j==0)or(i==0 or i==3 or i==6)or (j==4 and i>3)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("\n")
# FOR CREATING 7
for i in range(7):
    for j in range(5):
        if (( j==4)or(i==0 )): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("\n")
# FOR CREATING 9
for i in range(7):
    for j in range(5):
        if ((i<3 and j==0)or(i==0 or i==3 or i==6)or (j==4)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()

print("\n")
#CREATING A:
for i in range(6):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)): #for row=i, col=j
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("\n")

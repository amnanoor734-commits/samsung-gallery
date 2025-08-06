a = 15
b = 20
c = 12
if (a > b and a > c):
    print(a, "is greatest")
elif (b > c and b > a):
    print(b, " is greatest")
else:
    print(c, "is greatest")
i = 1
while (i <= 100):
    print(i)
    i = i + 1
#qbreak
print("\n")
for i in range(1, 101, 1):
    print(i, end=" ")
    if (i == 50):
        break
    else:
        print("Mississippi")
print("Thank you")
#continue
print("\n")
for i in range(10):
    if (i % 2 != 0):# skip iteration that donot based on modulus use % ,!=0 not equal to zero
        continue
    print(i)
#else and elif
print("\n")
a=22
if a>9:
    print("greater")
else:
    print("lesser")
print("\n")
h=19
if h>=18:
    print("yes")
else:
    print("outside the range")
#excersice  chap 6
r=8
r1=7
r2=2
r3=99
greatest=r
if r1>greatest:
    greatest=r1
if r2>greatest:
    greatest=r2
if r3>greatest:
    greatest=r3
else:
    print("none")
print("greatest of all",greatest)
#q2
math=99
phy=66
chem=77
total=math+phy+chem
percentage=(total/300)*100
if percentage<33 or percentage<40:
    print("fail")
if percentage>33 or percentage>40:
    print("pass")
if percentage<=33 or percentage<=40:
    print("pass")
print("\n")
#q3
comment = input("Enter your comment: ")

if ("make a lot of money" in comment.lower() or
    "buy now" in comment.lower() or
    "subscribe this" in comment.lower() or
    "click this" in comment.lower()):
    print("Spam comment detected!")
else:
    print("This comment is not spam.")

#q4
user=input("enter your user name:")
if len(user)<3:
    print("not possible")
else:
    print("nice username",user)
#q5
list=['nam','amna','nim','fa']
check=input("enter name:")
if check in list:
    print("name in list.")
else:
    print("name not  in list.")    
#q6
i=int(input("enter your marks :"))
if i>90 and i<=100:
    print("excellent.")
elif i>80 and i<=90:
    print("A")
elif i>70 and i<=80:
    print("B")
elif i>60 and i<=70:
    print("C")
elif i>50 and i<=60:
    print("D")
elif i<50:
    print("F")
else:
    print("not possible")



        
    

    
    
    
       
    



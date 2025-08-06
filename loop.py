#while loop:
count=1
while count<=7:
    print("hello")
    count =count +1
print(count)
o=5
while o>=1:
    print(o)
    o-=1

print("loop ended")
#practice question
h=1
while h<=100:
    print(h)
    h+=1
#q2
e=1
while e>=100:
    print(e)
    e-=1
#q3
n=1
while n<=10:
    print(2*n)
    n+=1
#q4 traverse
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1

#q5
nums=[1,4,9,16,25,36,49,64,81,100,36]
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx",i)
    else:
        print("finding..")   
    i+=1












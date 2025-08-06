universe_age = 14_000_000_000
print(universe_age)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[2])
print(bicycles[3].title()) #string method title capitilized the first letter that written in square bracket that is starts from0,1,2...
bick = ['trek', 'cannondale', 'redline', 'specialized']
print(bick[-2]) #position detection (-) starts from last to first

#Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message) #f string is used for composing message use in f"my{etc}"

#excersice : Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.
names=['unzila','hiba','aatika']
print(names[0]) ,print(names[1]), print(names[2])
message = f"hello all of you {names}."
print(message)

# List of favorite modes of transportation
transport = ["Honda motorcycle", "Tesla car", "Yamaha bike", "Toyota Corolla", "BMW sports car"]
# Print a statement about each one
print("I would like to own a " + transport[0] + ".")
print("I would like to drive a " + transport[1] + ".")
print("I would like to ride a " + transport[2] + ".")
print("I would like to have a " + transport[3] + ".")
print("I dream of owning a " + transport[4] + ".")

#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"First motorcycle I owned was a {first_owned}")

list = ['unzila', 'fiza', 'fatima']
print(f"welcome you at my house ", list[0])
print(f"welcome you at my house" , list[1])
print(f"welcome you at my house" , list[2])
list.remove("fatima")
print(list)
list.append("ash")
print(list)
unable_to_attend=["fatima"]
print(f"dear i would be honored to invite you",list[0])
print(f"dear i would be honored to invite you",list[1])
print(f"dear i would be honored to invite you",list[2])
print(f"dear {unable_to_attend[0]} unfortunately canot attend dinner but we stil looking forward to you")
list.insert(0, "Maira")                  # Beginning
list.insert(2, "Maya")  # Middle
list.append("Sara") 
print(f"Dear {list[0]}, you are invited to dinner. Looking forward to seeing you!")
print(f"Dear {list[1]}, you are invited to dinner. Looking forward to seeing you!")
print(f"Dear {list[2]}, you are invited to dinner. Looking forward to seeing you!")
print(f"Dear {list[3]}, you are invited to dinner. Looking forward to seeing you!")
print(f"Dear {list[4]}, you are invited to dinner. Looking forward to seeing you!")
print(f"Dear {list[5]}, you are invited to dinner. Looking forward to seeing you!")
print(list)
# question using pop
removed_list = list.pop()
print(f"Sorry {removed_list}, I can't invite you to dinner.")
removed_list = list.pop()
print(f"Sorry {removed_list}, I can't invite you to dinner.")
removed_list = list.pop()
print(f"Sorry {removed_list}, I can't invite you to dinner.")
removed_list = list.pop()
print(f"Sorry {removed_list}, I can't invite you to dinner.")

print(f"{list[0]}, you're still invited")
print(f"{list[1]}, you're still invited")
print(list)

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
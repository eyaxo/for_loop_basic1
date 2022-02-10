# Basic
for v in range(0,151): 
    print(v)
#Multiples of Five
for z in range(5,1000,5): 
    print(z)
# Counting the Dojo Way
for x in range(1,101):
    if x%10 == 0:
        print("Coding Dojo")
    if x%5 == 0:
        print("Coding")
    else:   
        print(x)
# Woah. That Sucker's Huge 
sum = 0
for y in range(0,500001):
    if y % 2 != 0:
        sum +=y
print(sum)
# Countdown by Fours
for p in range(2018,-1,-4):
    print(p)
# Flexible Counter
lowNum = 2
highNum = 12
mult = 4
for o in range(lowNum,highNum,mult):
    print(o)
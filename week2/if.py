import random
n=random.randint(1,100)
print("guess the number")
while True:
    x=int(input("enter the number"))
    if(x<n):
        print("too low")
    elif(x>n):
        print("too high")
    else:
        print("equal")
        break

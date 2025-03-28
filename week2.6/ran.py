import random
n=random.randint(1,100)
print("guess the number \n")
print("you have olny 5 chances")
x=1
while (x<5):
    guess=int(input("guess the number"))
    if guess==n:
       print("you won")
    break
    elif x==4:
        print("\t your chances are over")
    print("\t\t TRY AGAIN ")
    break 
    elif guess<n:
        print("your guess is low")
    x+=1        
    else guess>n:
        print("u guess is high")
        x+=1

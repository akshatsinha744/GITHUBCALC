import random

rand_no= random.randint(1,3)
print("comp turn:snake(s),water(w),gun(g)")
you = input("your turn:snake(s),water(w),gun(g)")
if(rand_no==1):
    comp='s'
elif(rand_no==2):
    comp='w'
elif(rand_no==3):
    comp='g'

def gameWin(comp,you):
    if(comp==you):
        return None
    elif(comp=='s'):
        if(you=='g'):
            return True
        if(you=='w'):
            return False
    elif(comp=='w'):
        if(you == 'g'):
            return False
        if(you=='s'):
            return True
    elif(comp=='g'):
        if(you=='w'):
            return True
        if(you=='s'):
            return False
print(f"comp choice={comp}")
a = gameWin(comp,you)
if a == None:
    print("This is a tie")
elif a == True:
    print("you win")
else:
    print("you lose")


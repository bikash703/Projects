import random
def gameWin(comp,you):
    if(comp==you):
        return None
    elif(comp=='s'):
        if(you=='w'):
            return False
        elif(you=='g'):
            return True
    elif(comp=='w'):
        if(you=='g'):
            return False
        elif(you=='s'):
            return True
    elif(comp=='g'):
        if(you=='s'):
            return False
        elif(you=='w'):
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)")
rand = random.randint(1, 3)
if(rand==1):
    comp='s'
elif(rand==2):
    comp='w'
elif(rand==3):
    comp='g'

you=input("Your Turn: Snake(s) Water(w) or Gun(g)")
a=gameWin(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if(a==None):
    print("Your Match is Tie")
elif(a):
    print("you win!")
else:
    print("you lose!")
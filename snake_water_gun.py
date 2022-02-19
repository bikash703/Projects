import random

def Gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print('computer turn: Snake(s), Water(w), Gun(g):-')
rand=random.randint(1,3)

if rand == 1:
    comp = 's'
elif rand==2:
    comp='w'
elif rand==3:
    comp='g'

you=input('Your turn: Snake(s), Water(w), Gun(g):- ')

print(f'Computer choice is {comp}')
print(f'Your choice is {you}')

a=Gamewin(comp,you)
if a==None:
    print('Match is tie')
elif a:
    print('You win')
else:
    print('You loss')


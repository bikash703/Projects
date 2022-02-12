import random
randno=random.randint(1,100)
userguess=None
guess=0
while userguess != randno:
    userguess=int(input('Enter Your Guess :- '))
    if userguess == randno:
        print('Your Guess is Right!!')
    else:
        if userguess > randno:
            print('You Guessed Wrong!,Enter a Smaller Number')
        else:
            print('You Guessed Wrong!,Enter a Larger Number')
        guess +=1
print(f'You Guess The Number is {guess} guesses')

with open('highscore.txt','r') as f:
    score = f.read()
if score =='':
    with open('highscore.txt','w') as f:
        f.write(str(guess))
elif guess < int(score) :
    with open('highscore.txt','w') as f:
        f.write(str(guess))




import random

userPoints=0
computerPoints=0

def rockPaperScissor(userOption, computerOption):
    global userPoints, computerPoints
    if(userOption==computerOption):
        winner='Match Drawn'
    else:
        if(userOption=='Rock'):
            if(computerOption=='Paper'):
                winner='Computer Won'
                computerPoints+=1
            else:
                winner='You Won'
                userPoints+=1
        elif(userOption=='Paper'):
            if(computerOption=='Rock'):
                winner='You Won'
                userPoints+=1
            else:
                winner='Computer Won'
                computerPoints+=1
        else:
            if(computerOption=='Rock'):
                winner='Computer Won'
                computerPoints+=1
            else:
                winner='You Won'
                userPoints+=1
    return winner

def snakeWaterGun(userOption, computerOption):
    global userPoints, computerPoints
    if(userOption==computerOption):
        winner='Match Drawn'
    else:
        if(userOption=='Snake'):
            if(computerOption=='Water'):
                winner='You Won'
                userPoints+=1
            else:
                winner='Computer Won'
                computerPoints+=1
        elif(userOption=='Water'):
            if(computerOption=='Snake'):
                winner='Computer Won'
                computerPoints+=1
            else:
                winner='You Won'
                userPoints+=1
        else:
            if(computerOption=='Snake'):
                winner='You Won'
                userPoints+=1
            else:
                winner='Computer Won'
                computerPoints+=1
    return winner


numberOfIterations=int(input("Enter the Number of Times you want to play: "))
iterationNumber=0

nameSwitch = int(input("Press 1 for Rock Paper Scissor, 2 for Snake Water Gun: "))
if(nameSwitch==2):
    nameList = ['Snake','Water','Gun']
    while(iterationNumber<numberOfIterations):
        userOption = int(input('Enter 1 for Snake, 2 for Water, 3 for Gun: '))
        if(userOption==1):
            userOption='Snake'
        elif(userOption==2):
            userOption='Water'
        else:
            userOption='Gun'
        computerOption=random.choice(nameList)
        winner=snakeWaterGun(userOption, computerOption)
        print(f"You chose {userOption}\nComputer chose {computerOption}\n{winner} this battle\n\n")
        print(f"Your Points till now: {userPoints}\nComputer Points till now: {computerPoints}")
        iterationNumber+=1

else:
    nameList = ['Rock','Paper','Scissor']
    while(iterationNumber<numberOfIterations):
        userOption = int(input('Enter 1 for Rock, 2 for Paper, 3 for Scissor: '))
        if(userOption==1):
            userOption='Rock'
        elif(userOption==2):
            userOption='Paper'
        else:
            userOption='Scissor'
        computerOption=random.choice(nameList)
        winner=rockPaperScissor(userOption, computerOption)
        print(f"You chose {userOption}\nComputer chose {computerOption}\n{winner}\n\n")
        print(f"Your Points till now: {userPoints}\nComputer Points till now: {computerPoints}")
        iterationNumber+=1



if(userPoints>computerPoints):
    print("\n\nYou won the game")
elif(computerOption>userPoints):
    print("\n\nComputer won the game")
else:
    print("\n\nMatch Drawn")
    
    


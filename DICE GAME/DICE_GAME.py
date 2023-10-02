def rolldice():
    score1 = 0
    score2 = 0
    import random
    for i in range(1,11):
        dice1 = random.randint(1,6) + random.randint(1,6)
        dice2 = random.randint(1,6) + random.randint(1,6)
        
        if dice1 > dice2:
            print(f'Player One score: {dice1}')
            print(f'Player Two score: {dice2}')
            print(f'Player One wins')
            score1 +=5
        elif dice2 > dice1:
            print(f'Player One score: {dice1}')
            print(f'Player Two score: {dice2}')
            print(f'Player Two wins')
            score1 +=5 
        else:
            print(f'Player one score: {dice1}')
            print(f'Player Two score: {dice2}')
            print(f'Its a draw')
            score1 +=1
            score2 += 1
            
    if score1 > score2:
        print(f'Player one is the overall winner by {score1} point')
    elif score1 > score2:
        print(f'Player one is the overall winner by {score1} point')
    else:
        print('Its a draw')
rolldice()

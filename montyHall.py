import random
A=''
B=''
C=''
door=''

counter=0
loops=10000

for i in range(loops):
    
    numList=[]
    totalNums=[1,2,3]
    num=random.randint(1,3)

    if num==1:
        A='goat'
        B='goat'
        C='car'
    elif num==2:
        A='goat'
        B='car'
        C='goat'
    elif num==3:
        A='car'
        B='goat'
        C='goat'

    #player picks a door
    player_Pick=random.randint(1,3)

    #goat doors get added to list
    if A=='goat':
        numList.append(1)
    if B=='goat':
        numList.append(2)
    if C=='goat':
        numList.append(3)

    #host picks a goat door
    while True:
        host_Pick=random.choice(numList)
        if host_Pick!=player_Pick:
            break
        else:
            continue

    #player switches to the other door
    totalNums.remove(host_Pick)
    totalNums.remove(player_Pick)
    player_Pick=totalNums[0]
    if player_Pick==1:
        door=A
    elif player_Pick==2:
        door=B
    else:
        door=C

    if door=='car':
        print('You win!')
        counter+=1

    else:
        print('You lose!')

winPct=counter/loops*100
print(winPct)











            

    

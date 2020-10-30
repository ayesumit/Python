print(RockPaperScissors)
 
 
def comp():
    x = random(0, 2)
    if x == 0:
        print('rock')
    if x ==1:
        print('paper')
    if x ==2:
        print('scissors')
def human():
rps=input('r, p, s - ')
if rps == 'r':
   print('rock') 
if rps == 'p':
    print('paper')
if rps == 's':
    print('scissors')
def result():
    human()
    comp()
if x == 0 and y == 0 or x== 1 and y ==1 or x ==2 or y == 2:
    print('draw')
if x == 0 and y == 2 or x == 1 and y == 0 or x == 2 and y == 1:
    print('u lose')
if x == 0 and y == 1 or x == 1 and y == 2 or x == 2 and y == 0:
    print('u lose')

import os
import random as r
ts = os.get_terminal_size().columns
computer = {0:"SNAKE",1:'WATER',2:"GUN"}
print("Welcome to SNAKE-WATER-GUN".center(ts))
print()
print()
print("SNAKE    WATER   GUN".center(ts))
print()

index = 0
score = 0


def draw():
    pass
def win():
    global index, score
    index += 1
    score += 2
def loss():
    global index, score
    if(score > 0):
        index += 1
        score -= 1

def checkScore(p,c):
    if p == "EXIT":
        print("Your Score: ",score)
        import author
        return exit()
    else:
        match p:
            case "SNAKE":
                match c:
                    case "SNAKE":
                        draw()
                    case "WATER":
                        win()
                    case "GUN":
                        loss()
            case "WATER":
                match c:
                    case "SNAKE":
                        loss()
                    case "WATER":
                        draw()
                    case GUN:
                        win()
            case "GUN":
                match c:
                    case "SNAKE":
                        win()
                    case "WATER":
                        loss()
                    case "GUN":
                        draw()
               
        

def text():
    print("Computer Turn:" , turnCom)
    print("Your Score: ",score)
    print()

while True:
    turnCom = r.choice(computer)
    player = input("TAKE YOUR TURN: ").upper()
    checkScore(player,turnCom)
    text()


    if index > 10 and score > 8:
        print("You Win!!!")
        index = score = 0
        import author
        break
    elif index > 10 and score < 8:
        print("You Loss!!!")
        index = score = 0
        import author
        break

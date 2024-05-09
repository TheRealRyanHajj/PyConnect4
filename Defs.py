import random as r, pygame
pygame.init()

def init():
    global window
    window = pygame.display.set_mode([700, 600])
    ### --- Board Set-Up --- ###
    # R = red chip | Y = yellow chip | * = Blank
    board = [
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"]
    ]
    return board

def displayBoard(board):
    global window
    for i in range(6):
        for j in range(7):
            chip = board[i][j]
            x,y = (j*100)+50,(i*100)+50
            if chip == "*":
                pass
            elif chip == "R":
                pygame.draw.circle(window, (255,0,0), (x,y), 46)
                pygame.draw.circle(window, (179,0,0), (x,y), 46, 8)
            elif chip == "Y":
                pygame.draw.circle(window, (255,255,0), (x,y), 46)
                pygame.draw.circle(window, (179,179,0), (x,y), 46, 8)

def flip():
    global window
    pygame.display.flip()

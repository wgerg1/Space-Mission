WIDTH = 750
HEIGHT = 750
PlayerX =375
PlayerY =375
def draw():
    screen.blit(images.backdrop,(0,0))
    screen.blit(images.astronaut,(PlayerX,PlayerY))
def update():
    global PlayerX, PlayerY
    if keyboard.right:
        PlayerX = PlayerX+1
    elif keyboard.down:
        PlayerY = PlayerY+1
    elif keyboard.up:
        PlayerY = PlayerY-1
    elif keyboard.left:
        PlayerX = PlayerX-1

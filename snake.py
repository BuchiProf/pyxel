import pyxel
from random import randint
TITLE = "Buchi'Snake"
WIDTH = 200 
HEIGHT = 160 
CASE = 20 
pyxel.init(WIDTH, HEIGHT, title = TITLE, fps=3)
snake = [[3, 3], [2, 3], [1, 3]]
direction = [1, 0]
score = 0
FRAME_REFRESH = 15
food = [8, 3]

def draw():
    pyxel.cls(0)
    for anneau in snake[1:] :
        x, y = anneau[0], anneau[1]
        pyxel.rect(x * CASE, y * CASE, CASE, CASE, 11)
        x_head, y_head = snake[0]
        pyxel.rect(x_head * CASE, y_head * CASE, CASE, CASE, 9)
    
    x_food, y_food = food
    pyxel.rect(x_food * CASE, y_food * CASE, CASE, CASE, 8)
    
    pyxel.text(4, 4, f"SCORE : {score}", 7)
    
def update():
    global direction, score, food
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    if head[0] >= WIDTH/CASE:
        head[0] = 0
    if head[0] < 0:
        head[0] = WIDTH/CASE - 1
    if head[1] >= HEIGHT/CASE:
        head[1] = 0
    if head[1] < 0:
        head[1] = HEIGHT/CASE - 1
    if head in snake[1:]:
        pyxel.cls(0)
        pyxel.text(4, 50, "Perdu, recharger la page", 7)
        pyxel.quit()
    snake.insert(0, head)
    
    
    if head == food:
        score += 1
        while food in snake:
            food = [randint(0, WIDTH/CASE - 1),
                    randint(0, HEIGHT/CASE -1)]
    else:
        snake.pop()
    if pyxel.btn(pyxel.KEY_ESCAPE) :
        exit()
    elif pyxel.btn(pyxel.KEY_LEFT) and direction in ([0, 1], [0, -1]):
        direction = [-1, 0]
    elif pyxel.btn(pyxel.KEY_RIGHT) and direction in ([0, 1], [0, -1]):
        direction = [1, 0]
    elif (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)) and direction in ([1, 0], [-1, 0]):
        direction = [0, -1]
    elif pyxel.btn(pyxel.KEY_DOWN) and direction in ([1, 0], [-1, 0]):
        direction = [0, 1]

pyxel.run(update, draw)



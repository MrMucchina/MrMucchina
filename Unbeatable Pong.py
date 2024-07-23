import pygame
import random

# Inizializza Pygame
pygame.init()

# Impostazioni di base
WIDTH, HEIGHT = 1200, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Imposta la finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Unbeatable Pong - by Mr_Mucchina')

# Variabili di gioco
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)
player_speed = 0
opponent_speed = 7
player_score = 0
opponent_score = 0



# Funzione per disegnare gli oggetti sullo schermo
def draw():
    font = pygame.font.Font(None, 74)
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    testo_giocatore="You: "+ str(player_score)
    player_text = font.render(str(testo_giocatore), True, WHITE)
    screen.blit(player_text, (WIDTH // 2 + 20, 10))
    testo_ai = "AI: " + str(opponent_score)
    opponent_text = font.render(str(testo_ai), True, WHITE)
    screen.blit(opponent_text, (WIDTH // 2 - 135, 10))
    testo_zero="(non oltrepasserai lo 0)"
    font=pygame.font.Font(None,30)
    zero_text = font.render(str(testo_zero), True, WHITE)
    screen.blit(zero_text, (WIDTH // 2 + 200, 3))

# Funzione per gestire il movimento della palla
def ball_movement():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        ball_restart()

    if ball.right >= WIDTH:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def game_movement():
    if ball.colliderect(player):
        get_2()
        ball_movement()

        opponent_movement()

# Funzione per gestire il movimento del giocatore
def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

# Funzione per gestire il movimento dell'avversario
def get_2():
    global x1, y1
    x1, y1 = ball.x, ball.y
    print("1     :", x1, y1)
    return x1, y1
def opponent_movement():
    x2, y2 =ball.x,ball.y
    print("2     :", x2, y2)
    offset = y1
    act_x = x2
    if x1==x2:
        x2-=1
    lato_x = x1 - x2
    lato_y = y1 - y2

    rapp = lato_y / lato_x

    direction = 1
    if y1 < y2 == 1:
        direction = -1
    if y1 > y2 == -1:
        direction = 1
    while act_x > 0:
        act_x -= 1
        lato_x += +1
        yn = lato_x * rapp
    yn = abs(-yn + offset)
    print(yn)
    while yn > HEIGHT:
        yn -= HEIGHT
        direction *= -1
    if direction == -1:
        yn = HEIGHT - yn
    print(yn)
    opponent.y=yn-70




# Funzione per resettare la palla al centro
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_y *= random.choice((-1, -1))
    ball_speed_x *= random.choice((-1, -1))
    get_2()
    ball_movement()
    opponent_movement()


# Loop principale del gioco
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 10
            if event.key == pygame.K_DOWN:
                player_speed += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 10
            if event.key == pygame.K_DOWN:
                player_speed -= 10

    get_2()
    ball_movement()
    opponent_movement()
    player_movement()
    ball_movement()


    draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

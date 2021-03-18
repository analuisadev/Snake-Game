"""
Snake Game: Jogo da Cobra
PS: Foram feitas algumas alterações referentes ao código do dia 100 em 100-Days-Of-Code.
"""

# Importações necessárias para a criação da janela

import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicialização das váriaveis e funções do pygame

pygame.init()

#Criação da váriavel para tocar a música durante o jogo

pygame.mixer.music.set_volume(0.1)
music = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

#Criação da váriavel para tocar o som quando houver colisões

collision_sound = pygame.mixer.Sound('smw_coin.wav')
collision_sound.set_volume(1)
# Criação da tela

width = 640
height = 480
x_snake = int(width / 2)
y_snake = int(height / 2)
velocity = 10
x_control = velocity
y_control = 0


# Definindo a fonte e tamanho do texto

font = pygame.font.SysFont('arial', 40, True, True)

# Criando váriaveis para assumir diferentes valores para cada colisão
x_apple = randint(40, 600)
y_apple = randint(50, 430)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
# Controlando a velocidade da movimentação do objeto

spots = 0
clock = pygame.time.Clock()
list_snake = []
initial_length = 5
death = False
#Função aumenta combra
def bigger_snake(list_snake):
    for XeY in list_snake:
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def restart_game():
    global spots, initial_length, x_snake, y_snake, list_snake, list_head, x_apple, y_apple, death
    spots = 0
    initial_length = 5
    x_snake = int(width / 2)
    y_snake = int(height / 2)
    list_snake = []
    list_head = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    death = False


#Looping principal do jogo

while True:
    clock.tick(30)
    screen.fill((255, 255, 255))
    msg = f'Pontos: {spots}'  # Mensagem
    text = font.render(msg, True, (0, 0, 0))  # Texto formatado
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # Criando uma condição para mudar a movimentação de acordo com a tecla

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == velocity:
                    pass
                else:
                    x_control = - velocity
                    y_control = 0
            if event.key == K_d:
                if x_control == - velocity:
                    pass
                else:
                    x_control = velocity
                    y_control = 0
            if event.key == K_w:
                if y_control == velocity:
                    pass
                else:
                    y_control = - velocity
                    x_control = 0
            if event.key == K_s:
                if y_control == - velocity:
                    pass
                else:
                    y_control = + velocity
                    x_control = 0

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control
#Desenhando Objetos dentro da Tela e movimentando
    snake = pygame.draw.rect(screen, (0, 255, 0), (x_snake, y_snake, 20, 20))  #
    apple = pygame.draw.rect(screen, (255, 0, 0), (x_apple, y_apple, 20, 20))
#Criando Condições para cada colisão
    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
#Adicionando os pontos
        spots = spots + 1
#Programando o som da colisão
        collision_sound.play()
#Aumento do comprimento da cobra
        initial_length = initial_length + 1

#Lista para armazenar os valores x e y da cobra
    list_head = []
    list_head.append(x_snake)
    list_head.append(y_snake)

    list_snake.append(list_head)

    if list_snake.count(list_head) > 1:
        font2 = pygame.font.SysFont('arial', 20, True, True)
        msg = 'Você se matou! Pressione "R" para jogar novamente'
        text = font2.render(msg, True, (0, 0, 0))
        ret_text = text.get_rect()
        death = True
        while death:
            screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                       restart_game()
            ret_text.center = (width//2, height//2)
            screen.blit(text, ret_text)
            pygame.display.update()

    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake < 0:
        y_snake = height
    if y_snake > height:
        y_snake = 0




    if len(list_snake) > initial_length:
        del list_snake[0]


    bigger_snake(list_snake)

    screen.blit(text, (450, 40))

    pygame.display.update()

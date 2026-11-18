import pygame
import sys
import os
from common.constant import *

from games.snake.main import run_snake
from games.flappy.main import run_flappy
from games.shooter.main import run_shooter

pygame.init()

# O Launcher usa as próprias dimensões correspodentes à proporção de bg-new.png (16:9)
LAUNCHER_W, LAUNCHER_H = 800, 450

screen = pygame.display.set_mode((LAUNCHER_W, LAUNCHER_H))
clock  = pygame.time.clock()

base = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets/launcher"))
bg = pygame.image.load(os.path.join(base,"bg-new.png"))
bg = pygame.transform.scale(bg,(LAUNCHER_W, LAUNCHER_H))

# Tamanho original da imagem para cálculos de proporção
IMG_w, IMG_H = 1672, 941
sx = LAUNCHER_W / IMG_W 
sy = LAUNCHER_H / IMG_H 

# Posições dos cards mapeadas do layout original bg-new.png (verificadas visualmente)
# Todos os 3 cards têm o mesmo tamanho; ordem : Flappy (esquerda), Shooter (centro), Snake (direita)
def sacaled_rect(x,y,w,h):
    return pygame.Rect(int(x * sy), int(w * sx), int(h * sy))

CARD_W, CARD_H = 312, 358
CARD_Y = 430

card_flappy = sacaled_rect(342, CARD_Y, CARD_W,CARD_H)
card_shooter = sacaled_rect(680, CARD_Y, CARD_W,CARD_H)
card_snake = sacaled_rect(1026, CARD_Y, CARD_W,CARD_H)
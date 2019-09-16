import pygame
from pygame.locals import *

simbolo = 'X'

tabuleiro = [ [ None, None, None ], \
              [ None, None, None ], \
              [ None, None, None ] ]

pygame.init()

tela = pygame.display.set_mode( (300, 300) )
pygame.display.set_caption('Jogo da Velha')

#desenhar o jogo
fundo = pygame.Surface((300,300))
fundo.fill((150,150,150))

#linhas verticais
pygame.draw.line(fundo, (0,0,0), (100, 0), (100, 300), 10)
pygame.draw.line(fundo, (0,0,0), (200, 0), (200, 300), 10)

#linhas horizontais
pygame.draw.line(fundo, (0,0,0), (0, 100), (300, 100), 10)
pygame.draw.line(fundo, (0,0,0), (0, 200), (300, 200), 10)

def posicao_tabuleiro(x, y):

    linha, coluna = 0, 0

    if (x < 100):
        coluna = 0
    elif (x < 200):
        coluna = 1
    else:
        coluna = 2

    if (y < 100):
        linha = 0
    elif (y < 200):
        linha = 1
    else:
        linha = 2

    return (linha, coluna)

def desenha_movimento(fundo, linha, coluna, simbolo):
    tabuleiro[linha][coluna] = simbolo

    centro_x = (coluna * 100) + 50
    centro_y = (linha * 100) + 50

    if (simbolo == 'O'):
        pygame.draw.circle(fundo, (0, 0, 0), (centro_x, centro_y), 35, 10)
    else:
        pygame.draw.line(fundo, (0,0,0), (centro_x - 23, centro_y - 23), (centro_x + 23, centro_y + 23), 10)
        pygame.draw.line(fundo, (0,0,0), (centro_x + 23, centro_y - 23), (centro_x - 23, centro_y + 23), 10)

def registra_clique(fundo):

    global grid, simbolo

    (x, y) = pygame.mouse.get_pos()
    (linha, coluna) = posicao_tabuleiro(x, y)

    if(tabuleiro[linha][coluna] is not None):
        return
    
    desenha_movimento(fundo, linha, coluna, simbolo)

    if (simbolo == 'X'):
        simbolo = 'O'
    else:
        simbolo = 'X'

def vencedor_jogo():
    for linha in tabuleiro:
        if linha[0] != None and linha[0] == linha[1] == linha[2]:
            return linha[0]

    for c in range(3):
        if tabuleiro[0][c] != None and tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c]:
            return tabuleiro[0][c]

    if tabuleiro[0][0] != None and tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    
    if tabuleiro[2][0] != None and tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2]:
        return tabuleiro[2][0]

    return None

rodando = True
vencedor = None

while rodando:
    #ver eventos de interação
    for event in pygame.event.get():
        if event.type is QUIT:
            rodando = False
        
        if vencedor is None and event.type is MOUSEBUTTONDOWN:
            registra_clique(fundo)
    
    #verificar se o estado é um fim de jogo
    vencedor = vencedor_jogo()
    if vencedor is not None:
        font = pygame.font.SysFont("Arial", 50)
        label = font.render(vencedor + " venceu!!", 1,  (255,255,255))
        tela.blit(fundo, (0, 0))
        tela.blit(label, (50, 125))
        pygame.display.flip()
        continue

    #atualizar a tela
    tela.blit(fundo, (0, 0))
    pygame.display.flip()


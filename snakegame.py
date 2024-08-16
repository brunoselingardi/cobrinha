#configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("jogo snake python")
tela = largura, altura = 600,400
pygame.display.set_mode((largura, altura))
relogio = pygame.time.clock()

#cores
preto = (0, 0, 0)
breanco = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

#parametros da cobra
tamanho_quadrado = 20
velocidade_cobra = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preto)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

        #desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        #desenhar_cobra

        #desenhar_pontos

        #atualização da tela
        pygame.display.update()
        relogio.pygame.tick(velocidade_cobra)

#loop infinito

#desenhar objetos na tela
#pontuação
#cobrinha
#comida

#logica de terminar o jogo
#o que acontece
#cobra bate na parede
#cobra bate na cobra

#interações do usuario
#fechou a tela
#teclas de mover

rodar_jogo()
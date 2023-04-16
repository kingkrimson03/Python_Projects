#jogo da velha usando o pygame
import pygame
pygame.init()

#criando a tela
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("Jogo da Velha")

#cores do jogo
black = (0,0,0)
white = (255,255,255)

#matriz de armazenamento das jogadas
jogadas= [['','',''],['','',''],['','','']]

#função para desenhar as linhas do jogo
def desenhar_linhas():
    for i in range(3):
        for j in range (3):
            pygame.draw.rect(screen,black,(i*100,j*100,100,2))
    for i in range (3):
        pygame.draw.rect(screen,black,(i*100,0,2,300))

#função para desenhar os simbolos dos jogadores no tabuleiro
def desenhar_simbolos():
    font = pygame.font.SysFont(None, 100)
    for i in range(3):
        for j in range(3):
            if jogadas[i][j] == 'X':
                symbol = font.render('X', True, black)
            elif jogadas[i][j] == 'O':
                symbol = font.render('O', True, black)
            else:
                continue
            screen.blit(symbol, (j*100+25, i*100))

#função para verificar se alguem ganhou
def verificar_vencedor():
    for i in range(3):
        if jogadas[i][0] == jogadas[i][1] == jogadas[i][2] != '':
            return jogadas[i][0]
        if jogadas[0][i] == jogadas[1][i] == jogadas[2][i] != '':
            return jogadas[0][i]
    if jogadas[0][0] == jogadas[1][1] == jogadas[2][2] != '':
        return jogadas[0][0]
    if jogadas[0][2] == jogadas[1][1] == jogadas[2][0] != '':
        return jogadas[0][2]
    return False

#loop principal do jogo
jogador = 'X'
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y =event.pos
            row = y // 100
            col = x // 100
            if jogadas[row][col] == '':
                jogadas[row][col] = jogador
                if verificar_vencedor():
                    print(jogador + ' GANHOU!!')
                    game_over = True 
                elif all(all(row) for row in jogadas):
                    print('EMPATE!!')
                    game_over = True
                else:
                    jogador = 'O' if jogador == 'X' else 'X'

    screen.fill(white)
    desenhar_linhas()
    desenhar_simbolos()
    pygame.display.update()

pygame.quit()
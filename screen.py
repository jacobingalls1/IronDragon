import pygame
from board import *

SCREEN = 800
HEX = True
initDir = "IronInit"

pygame.init()
gameBoard = Board()
gameBoard.setup(initDir)
board = gameBoard.getBoard()
gameBoard.doAdjacencies(HEX)
legend = gameBoard.getLegend()
clock = pygame.time.Clock()

xtile = SCREEN // len(board[0])
ytile = SCREEN // len(board)


pygame.display.set_icon(legend['J'].icon)
pygame.display.set_caption("Iron Dragon")
screen = pygame.display.set_mode((SCREEN, SCREEN))
mapBack = gameBoard.getMap()
mapBack = pygame.transform.scale(mapBack, (SCREEN, SCREEN))

def drawTrack(space1, space2):
    if HEX:
        pygame.draw.line(screen, (255, 0, 0), [xtile * (.5 + space1.posX + (.5 * (space1.posY % 2))), ytile * (.5 + space1.posY)], [xtile * (.5 + space2.posX + (.5 * (space2.posY % 2))), ytile * (.5 + space2.posY)], 1)
    else:
        pygame.draw.line(screen, (255, 0, 0), space1.pos(xtile, ytile), space2.pos(xtile, ytile), 1)

running = True
while running:
    screen.blit(mapBack, [0, 0])
    for i in range(len(board[0])):
        offset = 0
        if HEX:
            offset = .5 * (i % 2)
        for j in range(len(board)):
            screen.blit(board[i][j].cell.icon, [(.2 + j + offset) * xtile, (.2 + i) * ytile])
    # print(gameBoard.getAdjacencies())
    adj = gameBoard.getAdjacencies()
    for cell in adj.keys():
        for other in adj[cell]:
            drawTrack(cell, other[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.flip()
    clock.tick(2)

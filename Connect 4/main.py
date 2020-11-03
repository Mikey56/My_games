import pygame
from c4.board import Board
from c4.constants import WIDTH, HEIGHT

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

clock = pygame.time.Clock()
board = Board()

board.set_piece("R", 1)
board.set_piece("Y", 2)
board.set_piece("R", 2)
board.set_piece("R", 2)

run = True
while run:
    clock.tick(FPS)



    board.draw_grid(WIN)
    board.draw_pieces(WIN)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
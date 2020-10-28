#from .constants import WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE, WHITE, BLACK, SIDE_MARGIN, TOP_MARGIN, RED, BLUE
from .constants import *
import pygame
import random

class Piece:
    images_not_used_1 = list(range(12))
    random.shuffle(images_not_used_1)

    images_not_used_2 = list(range(12))
    random.shuffle(images_not_used_2)

    # images_team_1 = [img_1_1, img_2_1, img_3_1, img_4_1,
    #                  img_5_1, img_6_1, img_7_1, img_8_1,
    #                  img_9_1, img_10_1, img_11_1, img_12_1]
    # random.shuffle(images_team_1)
    #
    # images_team_2 = [img_1_2, img_2_2, img_3_2, img_4_2,
    #                  img_5_2, img_6_2, img_7_2, img_8_2,
    #                  img_9_2, img_10_2, img_11_2, img_12_2]
    # random.shuffle(images_team_2)


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False
        self.load_image_index()
        #self.load_image()
        self.cal_pos()

    # Change position of a piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.cal_pos()

    # Calculate the x and y cord of this piece
    def cal_pos(self):
        self.x_pos = SIDE_MARGIN + self.col * SQUARE_SIZE
        self.y_pos = TOP_MARGIN + self.row * SQUARE_SIZE

    # Set king
    def set_king(self):
        self.is_king = True

    # Draw piece on given window
    def draw_piece(self, win: pygame.Surface):
        if self.is_king:
            if self.color == WHITE:
                win.blit(img_king_1, (self.x_pos + 5, self.y_pos + 5))
            else:
                win.blit(img_king_2, (self.x_pos + 5, self.y_pos + 5))

        else:
            if self.color == WHITE:
                win.blit(images_1[self.image_index], (self.x_pos + 5, self.y_pos + 5))
            else:
                win.blit(images_2[self.image_index], (self.x_pos + 5, self.y_pos + 5))

            # x_mid = int(self.x_pos + SQUARE_SIZE//2)
            # y_mid = int(self.y_pos + SQUARE_SIZE//2)
            # pygame.draw.circle(win, BLUE, (x_mid, y_mid), 15)


    # Set image for new piece
    # def load_image(self):
    #     if self.color == WHITE:
    #         img_index = self.images_not_used_1.pop()
    #         self.image = pygame.image.load(f"checkers/Images/Team_1/img_{str(img_index)}.png")
    #         self.image_king = pygame.image.load(f"checkers/Images/Team_1/img_king.png")
    #
    #     else:
    #         img_index = self.images_not_used_2.pop()
    #         self.image = pygame.image.load(f"checkers/Images/Team_2/img_{str(img_index)}.png")
    #         self.image_king = pygame.image.load(f"checkers/Images/Team_2/img_king.png")

    # def load_image(self):
    #     if self.color == WHITE:
    #         self.image = self.images_team_1.pop()
    #         self.image_king = img_king_1
    #     else:
    #         self.image = self.images_team_2.pop()
    #         self.image_king = img_king_2

    def load_image_index(self):
        if self.color == WHITE:
            self.image_index = self.images_not_used_1.pop()
        else:
            self.image_index = self.images_not_used_2.pop()

    def __repr__(self):
        if self.color == WHITE:
            return f"!!!P({self.row}, {self.col}), WHITE!!!"
        else:
            return f"!!!P({self.row}, {self.col}), BLACK!!!"




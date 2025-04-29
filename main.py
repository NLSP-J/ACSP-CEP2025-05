import random
import word as w
import asyncio

word_list = ['eddgar','donald','yellow','bigger','nugget', 'mingos', 'papaya', 'thadus', 'bingus', 'alpaca', 'boongi', 'alferi', 'gerund', 'refund', 'beckon', 'reckon', 'hyenas', 'gravty', 'wordle', 'qwerty', 'fivegh','alferi','banana','rhythm']
ans = random.choice(word_list)
ans = 'yellow'

import pygame as pg
import time
pg.init()

win_width = 600
win_height = 800
screen = pg.display.set_mode([win_width, win_height])
pg.display.set_caption('hi')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
gray = (128, 128, 128)

font = pg.font.Font(None, 70)

game_board = [[' ', ' ', ' ', ' ', ' ', ' ',],
              [' ', ' ', ' ', ' ', ' ', ' ',],
              [' ', ' ', ' ', ' ', ' ', ' ',],
              [' ', ' ', ' ', ' ', ' ', ' ',],
              [' ', ' ', ' ', ' ', ' ', ' ',],
              [' ', ' ', ' ', ' ', ' ', ' ',],
              [' ', ' ', ' ', ' ', ' ', ' ',]]
count = 0
letters = 0
game_over = False
running = True
winner = False

def draw_board():
    for col in range(6):
        for row in range(7):
            square = pg.Rect(col * 100 + 12, row * 100 + 12, 75, 75)
            pg.draw.rect(screen, white, square, width = 2)

            letter_text = font.render(game_board[row][col], True, gray)
            screen.blit(letter_text, (col * 100 + 30, row * 100 + 30))
    rectangle = pg.Rect(6, count * 100 + 6, win_width - 10, 90)
    pg.draw.rect(screen, green, rectangle, width = 2)

def check_match():
    global game_over, winner
    for col in range(6):
        for row in range(7):
            highlight = pg.Rect(col * 100 + 12, row * 100 + 12, 75, 75)
            if ans[col] == game_board[row][col] and count > row:
                pg.draw.rect(screen, green, highlight)
            elif game_board[row][col] in ans and count > row:
                pg.draw.rect(screen, yellow, highlight)
    for row in range(7):
        guess = ''.join(game_board[row])
        if guess == ans and row < count:
            game_over = True
            winner = True

def draw_win():
    global game_over, running
    if count == 7 and not winner:
        game_over = True
        text = font.render('You lose!', True, white)
        screen.blit(text, (15, 710))
        pg.display.flip()
        time.sleep(2)
        running = False
    if game_over and winner:
        text = font.render('You win!', True, white)
        screen.blit(text, (15, 710))
        pg.display.flip()
        time.sleep(2)
        running = False

async def main():
    global running, letters, count
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.TEXTINPUT and letters < 6 and not game_over:
                entry = event.text
                if entry != ' ':
                    game_board[count][letters] = entry
                    letters += 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE and letters > 0:
                    game_board[count][letters - 1] = ' '
                    letters -=  1
                if letters == 6 and not game_over:
                    count += 1
                    letters = 0
                    break
        screen.fill(black)
        check_match()
        draw_board()
        draw_win()

        pg.display.update()
        await asyncio.sleep(0)

asyncio.run(main())

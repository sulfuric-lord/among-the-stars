import pygame
import random
import bg_stars as star
import character as ch
import items as it
import generators as gen
import os

#Константики
COLS = 30
ROWS = 30
pixel_const = 20

#Цвета ляляляля
BLACK = (0, 0, 0)
WALL_COL = (80, 255, 150) #Неоново - зеленый
PLAYER_COL = (255, 164, 32) #Неоново - оранжевый
STR_COL = (255, 20, 50)
DEX_COL = (50,205,50)
INT_COL = (0,191,255)
EXP_COL = (255,215,0)
item_col = (0,191,255)

BASE_DIR = os.path.dirname(__file__)
font_path = os.path.join(BASE_DIR, 'fonts', 'font.ttf')

pygame.init()
win = pygame.display.set_mode((COLS * pixel_const  + 350, ROWS * pixel_const))
pygame.display.set_caption("Dungeon, lol")
font = pygame.font.Font(font_path, 20)

gen.start_item_generate()
inventory = []

player_can_pickup = False
player_picking = False


def check_map():
    for i in default_map:
        for j in i:
            print(j, end="")
        print("")


run = True
while run:
    win.fill(BLACK)
    default_map = [["#" if i == 0 or i == COLS - 1 or j == 0 or j == ROWS - 1 else "." for i in range(COLS)] for j in range(ROWS)]
    current_map = default_map
    
    player_stats = [f"LEVEL 1. EXP: {ch.player.exp}" ,f"HP = {ch.player.hp}", f"STR = {ch.player.might}",
                    f"DEX = {ch.player.dex}", f"INT = {ch.player.intt}",
                    f"Weapon: {ch.player.weapon.name}", f"DMG: {ch.player.might * ch.player.weapon.min_dmg} - {ch.player.might * ch.player.weapon.max_dmg}"]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if ch.player.x + 1 < ROWS - 1:
                    ch.player.x += 1
            elif event.key == pygame.K_UP:
                if ch.player.x - 1 > 0:
                    ch.player.x -= 1
            elif event.key == pygame.K_RIGHT:
                if ch.player.y + 1 < COLS - 1:
                    ch.player.y += 1
            elif event.key == pygame.K_LEFT:
                if ch.player.y - 1 > 0:
                    ch.player.y -= 1
            elif event.key == pygame.K_i:
                if player_can_pickup:
                    player_picking = True
                    
            
    
    for i in range(len(current_map)):
        for j in range(len(current_map[i])):
            if current_map[i][j] == ".":
                pygame.draw.rect(win, BLACK, (i * pixel_const, j * pixel_const, pixel_const, pixel_const))
                
    if random.randint(0, 5) == 5:
        star.star_list.append(star.Stars(random.randint(0, COLS * pixel_const), random.randint(0, ROWS * pixel_const), random.randint(0, 5)))
    for i in star.star_list:
        pygame.draw.rect(win, i.color, (i.xpos, i.ypos, i.size, i.size))
        i.shine()
    
    
    current_map[ch.player.x][ch.player.y] = ch.player.look
    
    
    for i in gen.item_on_ground:
        current_map[i.x][i.y] = i
        if ch.player.x == i.x and ch.player.y == i.y:
            item_col = (255, 0, 180)
            player_can_pickup = True
            
            weapon_text = [f"{i.name}", f"{i.min_dmg} - {i.max_dmg} DMG"]
            y_text_pos = 550
            for item in weapon_text:
                text = font.render(item, False, (255, 255, 255))
                win.blit(text, (COLS * pixel_const + pixel_const, y_text_pos))
                y_text_pos += 20
            
            if player_picking:
                i.pick_up()
                player_picking = False
                player_can_pickup = False
        else:
            item_col = (0,191,255)  
                
                   
    y_text = 20
    for item in player_stats:
        stats_col = (255, 255, 255)
        if item == player_stats[2]:
            y_text += 10
        if item == player_stats[2]:
            stats_col = STR_COL
        elif item == player_stats[3]:
            stats_col = DEX_COL
        elif item == player_stats[4]:
            stats_col = INT_COL
        elif item == player_stats[0]:
            stats_col = EXP_COL
        stats_text = font.render(item, False, stats_col)
        win.blit(stats_text, (COLS * pixel_const + pixel_const, y_text))
        y_text += 20
    
    
    #Отрисовка обьектов
    for i in range(len(current_map)):
        for j in range(len(current_map[i])):
            if current_map[j][i] == "#":
                pygame.draw.rect(win, WALL_COL, (i * pixel_const, j * pixel_const, pixel_const, pixel_const))
            elif current_map[j][i] in gen.item_on_ground:
                pygame.draw.rect(win, item_col, (i * pixel_const, j * pixel_const, pixel_const, pixel_const))
    #Отрисовка Игрока:
        for i in range(len(current_map)):
            for j in range(len(current_map[i])):
                if current_map[j][i] == "@":
                    pygame.draw.rect(win, PLAYER_COL, (i * pixel_const, j * pixel_const, pixel_const, pixel_const))

    pygame.display.update()
import EGraphics as eg
import keyboard
import time
import PIL
import pygame
import random
import math

window = eg.create_window()
playerX, playerY = 50, 50  # player position
enemySpawn = time.time()  # enemy spawn delay

enemies = []
class Enemy:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)

    def update(self):
        global playerX, playerY
        speed = 0.05

        if self.x > playerX:
            self.x -= speed
        if self.x < playerX:
            self.x += speed
        if self.y > playerY:
            self.y -= speed
        if self.y < playerY:
            self.y += speed

def main_draw():
    eg.fill(window, (0, 0, 0))  # resenting screen
    eg.draw_circle(window, (255, 0, 0), playerX, playerY, 15)  # drawing player

    for enemy in enemies:  # basic enemies
        eg.draw_circle(window, (250, 205, 54), enemy.x, enemy.y, 20)

def movement():
    global playerX, playerY
    speed = 0.1

    if keyboard.is_pressed("shift"):
        speed = 0.15
    if keyboard.is_pressed("s"):
        playerY += speed
        if playerY >= 500:
            playerY = 500
    if keyboard.is_pressed("w"):
        playerY -= speed
        if playerY <= 0:
            playerY = 0.0
    if keyboard.is_pressed("a"):
        playerX -= speed
        if playerX <= 0:
            playerX = 0.0
    if keyboard.is_pressed("d"):
        playerX += speed
        if playerX >= 500:
            playerX = 500

    # normalization
    playerX = round(playerX, 1)
    playerY = round(playerY, 1)

# main menu
while True:
    eg.update()
    eg.draw_text(window, eg.color.hot_pink, 250, 200, "Trolerio", size=40, font='Showcard Gothic', draw_offset = "center")
    mx, my = eg.get_mouse_poz()
    if 250 - eg.get_text_size("START", 'Times New Roman', 30)[2] / 2 < mx < 250 + eg.get_text_size("START", 'Times New Roman', 40)[2] / 2 and 250 - eg.get_text_size("START", 'Times New Roman', 30)[3] / 2 < my < 250 + eg.get_text_size("START", 'Times New Roman', 40)[3] / 2:
        eg.draw_text(window, eg.color.green, 250, 250, "START", size=20, font='Times New Roman ', draw_offset="center")
        if eg.get_mouse_click()[0]:
            break
    else:
        eg.draw_text(window, eg.color.white, 250, 250, "START", size=20, font='Times New Roman', draw_offset="center")

# main loop
while True:
    
    if time.time() - enemySpawn >= 5:
        enemies.append(Enemy())
        enemySpawn = time.time()

    for enemy in enemies:
        enemy.update()

        if math.sqrt(abs(playerX - enemy.x) ** 2 + abs(playerY - enemy.y) ** 2) <= 35:
            eg.fill(window, (0, 0, 0))
            eg.draw_text(window, eg.color.red, 250, 200, "GAME OVER", size=40, draw_offset="center")
            eg.draw_text(window, eg.color.white, 250, 250, "press any key to end", size=15, draw_offset="center")
            pressed = True
            while True:
                eg.update()
                if keyboard.get_hotkey_name() != "":
                    if not pressed:
                        quit()
                else:
                    pressed = False

    movement()
    main_draw()
    eg.update()

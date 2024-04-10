
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame import *
import random
from collision import Collision
from level import Level
from player import Player
from rectangle import Rectangle
from bullet import Bullet

class Game:
    def init_game(self):        
        pygame.display.init()
        self.screen = pygame.display.set_mode((1200, 800), DOUBLEBUF|OPENGL)
        glClearColor(0.0,0.0,1.0,0.0)
        self.clock = pygame.time.Clock()
        self.ground = Rectangle(0,0,1200,70,[0.5,0.5,0.5])
        self.player = Player(50,40,[0.1,0.1,0.0])
        self.bulletsToShoot = []
        self.level0 = Level()
        self.coll = Collision()
        self.victory = False
        self.gameOver = False
        self.background_image = pygame.image.load('gameover.png').convert()
        self.bg_img = pygame.transform.scale(self.background_image,(1200,800))

    
    def update(self):
        delta_time = self.clock.tick() / 1000
        
        # Player movement
        if self.player.moveLeft:
            self.player.x -= self.player.speed * delta_time
        if self.player.moveRight:
            self.player.x += self.player.speed * delta_time

        # Shooting mechanism
        if self.player.isShooting:
            # Create the bullet to shoot
            bullet = Bullet((self.player.x + 20),(self.player.y + 50),500, 10, [1.0, 0.5, 0.0])
            self.bulletsToShoot.append(bullet)
            self.player.isShooting = False
        
        # Make the shots move in the game
        for shot in self.bulletsToShoot:
            if shot.y < 950:
                shot.y += shot.speed * delta_time
            else:
                self.bulletsToShoot.remove(shot)
    

        
        for enemy in self.level0.enemies:
            enemy.x += enemy.mov_speed_x* delta_time
            enemy.y += enemy.mov_speed_y* delta_time

        for enemy in self.level0.enemies:

            if round(enemy.x) >= 1200 - enemy.radius:
                enemy.mov_speed_x = -enemy.mov_speed_x
            if round(enemy.x) <= enemy.radius:
                enemy.mov_speed_x = -enemy.mov_speed_x
            if round(enemy.y) <= enemy.radius:
                enemy.mov_speed_y = -enemy.mov_speed_y
            if round(enemy.y) >= 800 - enemy.radius:
                enemy.mov_speed_y = -enemy.mov_speed_y
        
        # Check if player's shot hit the enemies and destroy the shot and the enemy
        for shot in self.bulletsToShoot:
            for enemy in self.level0.enemies:
                if(self.coll.circle_and_circle(enemy, shot)):
                    self.bulletsToShoot.remove(shot)
                    self.level0.enemies.remove(enemy) 
                    enemy.exists = False
               

        for enemy in self.level0.enemies:
             if(self.coll.circle_and_box(enemy, self.player)):
                    # print("BRUH")
                    self.gameOver = True


        if len(self.level0.enemies) == 0:
            self.victory = True
        
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glViewport(0, 0, 1200, 800)
        gluOrtho2D(0, 1200, 0, 800)
        glColor3f(0.1, 0.5, 0.0)

        # Draw player - he is in every level
        # Draw gun - it is in every level
        self.ground.draw_rectangle()
        self.player.draw_player()
        # Draw the bullets which the player is shooting
        for bullet in self.bulletsToShoot:
            bullet.draw_bullet()

        # Draw the levels
        self.level0.draw_level()
        pygame.display.flip()

    def gameOverScreen(self):
        textureSurface = pygame.image.load('gameover.png')
        textureData = pygame.image.tostring(textureSurface,"RGBA",1)
        textureID = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 1200, 800, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(0,0)
        glTexCoord2f(0, 1)
        glVertex2f(0,800)
        glTexCoord2f(1, 1)
        glVertex2f(1200,800)
        glTexCoord2f(1, 0)
        glVertex2f(1200,0)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        pygame.display.flip()

    def victoryScreen(self):
        textureSurface = pygame.image.load('victory.png')
        textureData = pygame.image.tostring(textureSurface,"RGBA",1)
        textureID = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 1200, 800, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(0,0)
        glTexCoord2f(0, 1)
        glVertex2f(0,800)
        glTexCoord2f(1, 1)
        glVertex2f(1200,800)
        glTexCoord2f(1, 0)
        glVertex2f(1200,0)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        pygame.display.flip()


    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == K_LEFT:
                    self.player.moveLeft = True
                elif event.key == K_RIGHT:
                    self.player.moveRight = True
                elif event.key == K_SPACE:
                    self.player.isShooting = True
            elif event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    self.player.moveLeft = False
                elif event.key == K_RIGHT:
                    self.player.moveRight = False
                elif event.key == K_SPACE:
                    self.player.isShooting = False
        self.update()
        if self.victory :
            self.victoryScreen()
        elif self.gameOver:
            self.gameOverScreen()
        else:
            self.display()

        
    
if __name__ == "__main__":
    game = Game()
    game.init_game()
    while True:
        game.game_loop()
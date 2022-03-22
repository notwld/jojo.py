import pygame as pg
from constants import *
import os

pg.init()

WIN = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("JOJO GAME")

sound = pg.mixer.music.load('Assets/bg-music.mp3')

pg.mixer.music.play(-1,0,0)

walkRight = [pg.image.load('Assets/going-right-1.png'), pg.image.load('Assets/going-right-2.png'), pg.image.load('Assets/going-right-3.png'), pg.image.load('Assets/going-right-4.png'), pg.image.load('Assets/going-right-5.png'), pg.image.load('Assets/going-right-6.png'), pg.image.load('Assets/going-right-7.png'), pg.image.load('Assets/going-right-8.png'), pg.image.load('Assets/going-right-9.png')]

walkLeft = [pg.image.load('Assets/going-left-1.png'), pg.image.load('Assets/going-left-2.png'), pg.image.load('Assets/going-left-3.png'), pg.image.load('Assets/going-left-4.png'), pg.image.load('Assets/going-left-5.png'), pg.image.load('Assets/going-left-6.png'), pg.image.load('Assets/going-left-7.png'), pg.image.load('Assets/going-left-8.png'), pg.image.load('Assets/going-left-9.png')]


jump = [pg.image.load('Assets/jump-left.png'), pg.image.load('Assets/jump-right.png')]
crouch = [pg.image.load('Assets/crouch-left.png'), pg.image.load('Assets/crouch-right.png')]
attack = pg.image.load('Assets/attacking.png')
bg = pg.image.load('Assets/game_bg.png')

char = [pg.image.load('Assets/standing-right.png'),pg.image.load('Assets/standing-left.png')]


class player:
    def __init__(self,x,y,width,height,vel,isJump,isCrouch,jumpCount,isAttack,walkCount):
        self.x = x
        self.y = y
        self.ch_height = height
        self.ch_width = width
        self.vel = vel
        self.isJump = isJump
        self.rightJump = False
        self.leftJump = False
        self.jumpCount = jumpCount
        self.left = False
        self.right= False
        self.walkCount = walkCount
        self.standing = True
        self.isCrouch = isCrouch
        self.rightCrouch = False
        self.leftCrouch = False
        self.isAttack = isAttack

    def draw(self,win):
        
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not self.standing:

            if self.left:  
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y)) 
                self.walkCount += 1          

            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount+= 1
            
            elif self.rightCrouch:
                win.blit(crouch[0], (self.x,380))
            
            elif self.leftCrouch:
                win.blit(crouch[1], (self.x,380))
            
            elif self.isAttack:
                win.blit(attack, (self.x,self.y))
            

        else:

            if self.right:
                win.blit(char[0], (self.x,self.y))
                self.rightJump = True
                self.leftJump = False
                self.rightCrouch = True
                self.leftCrouch = False
            
            elif self.left:
                win.blit(char[1], (self.x,self.y))
                self.rightJump = False
                self.leftJump = True
                self.rightCrouch = False
                self.leftCrouch = True
                


            else:
                if self.isJump:
                    if self.rightJump:
                        win.blit(jump[1],(self.x,self.y))
                    else:
                        win.blit(jump[0],(self.x,self.y))
                else:
                    if self.leftJump:
                        win.blit(char[1],(self.x,self.y))
                    else:
                        win.blit(char[0],(self.x,self.y))

        
                    



man = player(X,Y,CH_WIDTH,CH_HEIGHT,VEL,isJump,isCrouch,jumpCount,isAttack,WALK_COUNT)


def game_draw():
    global WIN
    WIN.blit(bg,(0,0))
    man.draw(WIN)
    pg.display.update()

def main():

    clock = pg.time.Clock()
    global RUN,SCREEN_HEIGHT,SCREEN_WIDTH
    #gameloop

    while RUN:

        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUN = False
                
        KEYS = pg.key.get_pressed()

        if KEYS[pg.K_RIGHT] and man.x<SCREEN_WIDTH - man.ch_width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing=False

        elif KEYS[pg.K_LEFT] and man.x>man.vel:
            man.x -= man.vel
            man.right = False
            man.left = True
            man.standing=False
        
            
             
        elif KEYS[pg.K_DOWN]:
            man.isCrouch = True
            man.left = False
            man.right = False
            man.isJump = False
            man.standing = False

        elif KEYS[pg.K_SPACE]:
            ora = pg.mixer.music.load('Assets/ora.mp3')
            pg.mixer.music.play(0,0,0)
            man.isAttack = True
            man.isCrouch = False
            man.left = False
            man.right = False
            man.isJump = False
            man.standing = False
        
        else:
            man.standing=True
            man.walkCount = 0

        if not (man.isJump):
               
            if KEYS[pg.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        
        else:
            if man.jumpCount>=-10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1

                man.y -=(man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount-=1

            else:
                man.isJump=False
                man.jumpCount=10

        game_draw()
        

    pg.quit()

if __name__ == "__main__":
    main()


        

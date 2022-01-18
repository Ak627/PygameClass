import pygame
import math
pygame.init

#constants for colors
RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)
BROWN = (165, 42, 42)
BLUE = (20,0,102)

### class definition--------------------------------------------
class flower:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        pygame.draw.rect(screen, (GREEN), (self.xpos-10, self.ypos+20, 20, 100)) #(190, 330) is my top left corner
        pygame.draw.circle(screen, (RED), (self.xpos-20, self.ypos+20), 20) 
        pygame.draw.circle(screen, (RED), (self.xpos+20, self.ypos+20), 20) 
        pygame.draw.circle(screen, (RED), (self.xpos-20, self.ypos-20), 20) 
        #add missing petals here
        pygame.draw.circle(screen, (RED), (self.xpos+20, self.ypos+20), 20) 
        pygame.draw.circle(screen, (RED), (self.xpos+20, self.ypos-20), 20) 
        pygame.draw.circle(screen, (ORANGE), (self.xpos, self.ypos), 20) 
# end of class definition-----------------------------------------
class beetle:
    def __init__(self, xpos, ypos):
      self.xpos = xpos
      self.ypos = ypos

    def draw(self):
        pygame.draw.circle(screen, (BROWN), (self.xpos-20, self.ypos+30), 20)
        pygame.draw.circle(screen,(BROWN),(self.xpos+18, self.ypos+30), 30)
        pygame.draw.circle(screen, (RED), (self.xpos-20, self.ypos+30), 10)
        pygame.draw.rect(screen, (BLUE), (self.xpos+10, self.ypos+30, 5, 50))
        pygame.draw.rect(screen, (BLUE), (self.xpos+30, self.ypos+30, 5, 50))
        pygame.draw.arc(screen,(BROWN), (self.xpos-40, self.ypos-2, 20, 20),4* math.pi/3, math.pi/1, 5 )


#stamp (aka instantiate) flowers
flower1 = flower(200, 200)
flower2 = flower(400, 400)
flower3 = flower(100, 400)
flower4 = flower(300, 100)
flower5 = flower(450,250)
beetle1 = beetle(200, 400)
beetle2 = beetle(350, 500)
beetle3 = beetle(400, 100)



#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("flower class demo")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed


#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
 

    #draw class objects
    flower1.draw()
    flower2.draw()
    flower3.draw()
    flower4.draw()
    flower5.draw()
  
    beetle1.draw()
    beetle2.draw()
    beetle3.draw()

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()

import pygame

pygame.init()

ecran = pygame.display.set_mode((400,700))

pygame.display.set_caption('BRQuiz')

pygame.display.flip()


running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False


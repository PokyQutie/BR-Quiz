import pygame
import requests
from PIL import Image
from io import BytesIO

class buton:
    def __init__(self,imagine,actiune,pozitie):
        self.imagine = imagine
        self.actiune = actiune
        self.pozitie = pozitie

pygame.init()

ecran = pygame.display.set_mode((400,700))

pygame.display.set_caption('BRQuiz')

pygame.display.flip()

image_url = "https://i.ibb.co/k0rBN10/fundal.png"
response = requests.get(image_url, stream=True)
image_data = response.raw.read()
image_file = BytesIO(image_data)
image = Image.open(image_file)
image = image.convert('RGB')
image_data = image.tobytes()

# Get the image size (width and height)
width, height = image.size

# Create the Pygame surface from the data and size
surface = pygame.image.fromstring(image_data, (width, height), 'RGB')
ecran.blit(surface, (0, 0))
pygame.display.flip()

running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            '''#for i in butoane:
                if pos[0] >='''

      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False


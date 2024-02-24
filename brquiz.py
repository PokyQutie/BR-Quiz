import pygame
import requests
from PIL import Image
from io import BytesIO
import gspread

class buton:
    def __init__(self,url,actiune,pozitie):
        self.url = url
        self.actiune = actiune
        self.pozitie = pozitie

def import_img(url,poz):
    image_url = url
    response = requests.get(image_url, stream=True)
    image_data = response.raw.read()
    image_file = BytesIO(image_data)
    image = Image.open(image_file)
    image = image.convert('RGB')
    image_data = image.tobytes()
    width, height = image.size
    surface = pygame.image.fromstring(image_data, (width, height), 'RGB')
    ecran.blit(surface, poz)
    pygame.display.flip()
    
#start
pygame.init()
ecran = pygame.display.set_mode((400,700))
pygame.display.set_caption('BRQuiz')
pygame.display.flip()

#incarcare fundal
import_img("https://i.ibb.co/k0rBN10/fundal.png",(0,0))

credentials_file = "C:\\Users\\stefi\\Desktop\\br\\BR-Quiz\\br-quiz-415321-45910d66fccb.json"
gc = gspread.service_account(filename=credentials_file)

spreadsheet_id = "1LJjuzeEC3tc9mxYmxNyXAn-1-ykkUUS2JiIWdIbBO5s"
sheet = gc.open_by_key(spreadsheet_id)

worksheet = sheet.sheet1
cell = worksheet.cell(row=1, col=5)
nr_butt = int(cell.value)

butoane = []

for i in range(1,nr_butt+1):
    pula = buton(worksheet.cell(row=i+1, col=1).value, worksheet.cell(row=i+1, col=2).value, (int(worksheet.cell(row=i+1, col=3).value),int(worksheet.cell(row=i+1, col=4).value)))
    butoane.append(pula)

for i in butoane:
    print(i.pozitie)
    import_img(i.url, i.pozitie)


running = True
  
#loop 
while running:   
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            '''#for i in butoane:
                if pos[0] >='''

      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False


import pygame
import requests
from PIL import Image
from io import BytesIO
import gspread

class buton:
    def __init__(self,url,actiune,pozitie,lung,lat,ok=1):
        self.url = url
        self.actiune = actiune
        self.pozitie = pozitie
        self.lung = lung
        self.lat = lat
        self.ok = ok

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
import_img("https://i.ibb.co/RpSNH2h/tabbar.png",(0,630))
import_img("https://i.ibb.co/xFRRC8N/Captura-ecran-3.png",(175,5))

credentials_file = "C:\\Users\\stefi\\Desktop\\br\\BR-Quiz\\br-quiz-415321-45910d66fccb.json"
gc = gspread.service_account(filename=credentials_file)

spreadsheet_id = "1LJjuzeEC3tc9mxYmxNyXAn-1-ykkUUS2JiIWdIbBO5s"
spread2_id = "1d0AlEFfYroWltyLYTI7iEir2S4ND9HGDT9gxwpW6ZW4"
sheet = gc.open_by_key(spreadsheet_id)
shit = gc.open_by_key(spread2_id)

worksheet = sheet.sheet1
workshit = shit.sheet1
cell = worksheet.cell(row=1, col=7)
nr_butt = int(cell.value)

butoane = []

for i in range(1,nr_butt+1):
    pula = buton(worksheet.cell(row=i+1, col=1).value, int(worksheet.cell(row=i+1, col=2).value), (int(worksheet.cell(row=i+1, col=3).value),int(worksheet.cell(row=i+1, col=4).value)),int(worksheet.cell(row=i+1,col=5).value),int(worksheet.cell(row=i+1,col=6).value))
    butoane.append(pula)

for i in butoane:
    import_img(i.url, i.pozitie)


running = True
  
#loop 
while running:   
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in butoane:
                if pos[0] >= i.pozitie[0] and pos[1] >= i.pozitie[1] and pos[0] <= i.pozitie[0]+i.lung and pos[1] <= i.pozitie[1]+i.lat:
                    if i.actiune%3 == 0:
                        import_img("https://i.ibb.co/k0rBN10/fundal.png",(0,0))
                        nr_int = int(workshit.cell(row=1, col=1).value)
                        for j in range(1,nr_int+1):
                            if int(workshit.cell(row=j+1, col=2).value) == i.actiune:
                                for k in range(1, int(workshit.cell(row=j+1, col=3).value)*2,2):
                                    import_img(workshit.cell(row=j+1,col=4+k).value,(5,5))
                                    import_img(workshit.cell(row=j+1,col=4+k+1).value,(5,700-201))
                                    ok=0
                                    while ok == 0: #5 201
                                        for event in pygame.event.get(): 
                                            if event.type == pygame.MOUSEBUTTONUP:
                                                pos = pygame.mouse.get_pos()
                                                if pos[1] >= 700-201:
                                                    ok=1
                                    
                            break
                        import_img("https://i.ibb.co/k0rBN10/fundal.png",(0,0))
                        
            if pos[1]>630:
                import_img("https://i.ibb.co/FhBZSRK/fundal-Copy.png",(0,0))
                import_img("https://i.ibb.co/RpSNH2h/tabbar.png",(0,630))
                while 1 != 0:
                    pass
            import_img("https://i.ibb.co/k0rBN10/fundal.png",(0,0))     
            import_img("https://i.ibb.co/RpSNH2h/tabbar.png",(0,630))
            import_img("https://i.ibb.co/xFRRC8N/Captura-ecran-3.png",(175,5))
            for i in butoane:
                import_img(i.url, i.pozitie)

      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False


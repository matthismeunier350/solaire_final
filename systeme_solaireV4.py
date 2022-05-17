#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Tue Jan 25 14:31:51 2022

Système Solaire

@author: matthis
"""

import pygame 
import math
import time
import np
import button

pygame.init()

L = 1300
H=800
big_screen = pygame.display.set_mode((L, H))

little_screen = pygame.display.set_mode((100, 400))

largeur = 1600
hauteur = 800
screen = pygame.display.set_mode((largeur, hauteur))
middle_screen = (1300/2, 800/2)
img_play = pygame.image.load('Système Solaire/S.jpeg')

BG = (0, 0, 0)
white = (255,255,255)
font = pygame.font.Font(None, 30)
Font = pygame.font.Font(None, 30)
pause  = False

base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(1350, 650, 140, 50)
  

color_active = pygame.Color('lightskyblue3')
  

color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False






data = {'A' :['Mercure', 'poids = 3,33 x 10^23 kg', 'rayon = 4200 km', 'distance soleil = 46 à 70 mm km', 'temps de rotation = 87,969 j', 'température moyenne = 462°C', "Système solaire/MERCURE.jpeg",'A'],
                'B' : ['Venus','poids = 4,867 5x10^24 kg', 'rayon = 6050 km', 'distance soleil = 104 mm km', 'temps de rotation = 243 j', 'température moyenne = 440°C',"Système solaire/VENUS.jpeg"],
                'C' : ['La Terre','poids = 5,973 x 10^24 kg', 'rayon = 6378 km', 'distance soleil = 150 mm km', 'temps de rotation = 365 j', 'température moyenne = 14°C',"Système solaire/TERRE.jpeg"],
                'D' : ['Mars', 'poids = 6,418 x 10^23 kg','rayon = 3 396 km', 'distance soleil = 227 mm km', 'temps de rotation = 696 j', 'température moyenne = -60°C',"Système solaire/MARS.jpeg"],
                'E' : ['Jupiter', 'poids = 1,89 X 10^17 kg', 'rayon = 71 492 km', 'distance soleil = 778 mm km', 'temps de rotation = 11 ans 315 j', 'température moyenne = -163°C',"Système solaire/JUPITER.jpeg"],
                'F' : ['Saturne', 'poids = 5,68 X 10^26 kg', 'rayon = 58 232 km', 'distance soleil = 1,4 md km', 'temps de rotation = 29 ans et 167 j', 'température moyenne = -189°C',"Système solaire/SATURNE.jpeg"],
                'G' : ['Uranus', 'poids = 8,6 X 10^25 kg', 'rayon = 51 118 km','distance soleil = 2,8 md km', 'temps de rotation = 84 ans', 'température moyenne = -218°C',"Système solaire/URANUS.jpg"],
                'H' : ['Neptune', 'poids = 102 X 10^24 kg', 'rayon = 24 764 km', 'distance soleil = 4,5 md km', 'temps de rotation = 165 ans', 'température moyenne = -220°C',"Système solaire/NEPTUNE.jpeg"]}


d=1

Pleinelune = '/Users/matthis/Desktop/lune/14.png'
Nouvellelune = '/Users/matthis/Desktop/lune/01.png'
lune_croissante = '/Users/matthis/Desktop/lune/04.png'
premier_quartier = '/Users/matthis/Desktop/lune/07.png'
lune_decroissant = '/Users/matthis/Desktop/lune/21.png'
dernier_quartier = '/Users/matthis/Desktop/lune/19.png' 


da={"02:01:2022":Nouvellelune,"05:01:2022":lune_croissante,"08:01:2022":premier_quartier,"16:01:2022":Pleinelune,"24:01:2022":dernier_quartier,"28:01:2022":lune_decroissant,"31:01:2022":Nouvellelune,"03:02:2022":lune_croissante,"07:02:2022":premier_quartier,"15:02:2022":Pleinelune,"23:02:2022":dernier_quartier,"26:02:2022":lune_decroissant,"02:03:2022":Nouvellelune,"05:03:2022":lune_croissante,"09:03:2022":premier_quartier,"17:03:2022":Pleinelune,"24:03:2022":dernier_quartier,"27:03:2022":lune_decroissant,"31:03:2022":Nouvellelune,"04:04:2022":lune_croissante,"08:04:2022":premier_quartier,"16:04:2022":Pleinelune,"22:04:2022":dernier_quartier,"26:04:2022":lune_decroissant,"30:04:2022":Nouvellelune,"03:05:2022":lune_croissante,"08:05:2022":premier_quartier,"15:05:2022":Pleinelune,"22:05:2022":dernier_quartier,"25:05:2022":lune_decroissant,"29:05:2022":Nouvellelune,"02:06:2022":lune_croissante,"06:06:2022":premier_quartier,"13:06:2022":Pleinelune,"20:06:2022":dernier_quartier,"24:06:2022":lune_decroissant,"28:06:2022":Nouvellelune,"02:07:2022":lune_croissante,"06:07:2022":premier_quartier,"13:07:2022":Pleinelune,"19:07:2022":dernier_quartier,"23:07:2022":lune_decroissant,"27:07:2022":Nouvellelune,"31:07:2022":lune_croissante,"04:08:2022":premier_quartier,"11:08:2022":Pleinelune,"18:08:2022":dernier_quartier,"22:08:2022":
lune_decroissant,"26:08:2022":Nouvellelune,"30:08:2022":lune_croissante,"03:09:2022":premier_quartier,"09:09:2022":Pleinelune,"16:09:2022":dernier_quartier,"21:09:2022":lune_decroissant,"25:09:2022":Nouvellelune,"28:09:2022":lune_croissante,"02:10:2022":premier_quartier,"09:10:2022":Pleinelune,"16:10:2022":dernier_quartier,"20:10:2022":lune_decroissant,"24:10:2022":Nouvellelune,"28:10:2022":lune_croissante,"31:10:2022":premier_quartier,"07:11:2022":Pleinelune,"15:11:2022":dernier_quartier,"19:11:2022":lune_decroissant,"23:11:2022":Nouvellelune,"26:11:2022":lune_croissante,"29:11:2022":premier_quartier,"07:12:2022":Pleinelune,"15:12:2022":dernier_quartier,"19:12:2022":lune_decroissant,"22:12:2022":Nouvellelune,"26:12:2022":lune_croissante,"29:12:2022":premier_quartier}


recherche_pour= {Nouvellelune: '0', Pleinelune : '100', lune_croissante : '31', premier_quartier: '50',lune_decroissant:'37',dernier_quartier:'60'}

pourcentage = ['1','4','9','15','23','31','50','60','69','79','87','93','100','95','92','89','80','70','50','37','27','18','6','0']





lune = False

def dessine_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


import time

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image(Pleinelune))
        self.images.append(load_image('/Users/matthis/Desktop/lune/02.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/03.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/04.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/05.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/06.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/07.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/08.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/09.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/10.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/11.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/12.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/13.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/14.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/15.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/16.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/17.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/18.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/19.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/20.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/21.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/22.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/23.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/24.png'))
        # assuming both images are 64x64 pixels
        


        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(60, 60, 128, 128)
        self.index_pourcentage = 0
        self.pourcentage =  pourcentage
        self.pourcentages = self.pourcentage[self.index_pourcentage]

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        time.sleep(0.01)
    
    def uptade_pourcentage(self):
        da_pour = {self.images[0] : '1',self.images[1] : '4',self.images[2] : '9',self.images[3] : '15',self.images[4] : '23',self.images[5] : '31',self.images[6] : '50',self.images[7] : '60',self.images[8] : '69',self.images[9] : '79',self.images[10] : '87',self.images[11] : '93',self.images[12] : '100',self.images[13] : '95',self.images[14] : '92',self.images[15] : '89',self.images[16] : '80',self.images[17] : '70',self.images[18] : '50',self.images[19] : '37',self.images[20] : '27',self.images[21] : '18',self.images[22] : '18',self.images[23] : '6'}
        if da_pour.get(self.images[self.index]):

            dessine_text(f'pourcentage :{da_pour.get(self.images[self.index])}% ', font, (255,255,255), 30, 180)

            


class ecran():

    def __init__(self) -> None:
     
      def affichage_info(self) -> dict:

        for planete in data:
            if planete == data.key:
                return data.value
        
    def ecriture(self,planète):

        dataget = data[planète]

        text = font.render(dataget[0], 16, (0, 0, 0))

        poids = font.render(dataget[1], 16, (0, 0, 0))
        rayon = font.render(dataget[2], 1, (0, 0, 0))
        distance = font.render(dataget[3], 1, (0, 0, 0))
        rotation = font.render(dataget[4], 1, (0, 0, 0))
        temperature = font.render(dataget[5], 1, (0, 0, 0))

        screen.blit(text, (1320, 300))
        screen.blit(poids, (1320, 350))
        screen.blit(rayon, (1320, 400))
        screen.blit(distance, (1320, 450))
        screen.blit(rotation, (1320,500))
        screen.blit(temperature, (1320,550))

        img = pygame.image.load(dataget[-1])
        img = pygame.transform.scale(img, (280, 275))
        
        screen.blit(img, (1305, 20))
        pass
    
    def page_lune(self):
        pygame.draw.rect(screen, white, ((0, 0), (220, 220)))
        pygame.draw.rect(screen, (0,0,0), ((10, 10), (200, 200)))
        
        
    

def draw_bg():
	screen.fill(BG)

	text1 = "Entre date pour aligner les planete"

	pygame.draw.rect(screen, white, ((1300, 0), (1300, 800)))
	pygame.draw.line(screen, (0,0,0), (1300, 5), (1800, 5), 15)
	pygame.draw.line(screen, (0,0,0), (1300, 600), (1800, 600), 15)
	pygame.draw.line(screen, (0,0,0), (1595, 0), (1595, 800), 15)
	pygame.draw.line(screen, (0,0,0), (1300, 795), (1800, 795), 15)


    
class Soleil(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, name):
        pygame.sprite.Sprite.__init__(self)
        img =pygame.image.load(f'Système solaire/{name}')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.middle_screen = middle_screen
        self.t= 0
        self.x = np.cos(self.t) * 30
        self.y = np.sin(self.t) * 20 	
        self.name = 0
        self.v = 1
        self.a=(x,y)
        
        
    def lune(self, x: float, y: float,v, pos_terre) -> None :
        if pause:
            self.v = 0
        else:
            self.v = v
        self.t += 0.1*self.v*d
        self.x = np.cos(self.t) * 25
        self.y = np.sin(self.t) * 45
		
        self.rect.center = (pos_terre[0]+self.x, pos_terre[1]+self.y)
    
    def compteur_jour(self):
        pass

        

    def phase_lune(self):
        """
        img1 =pygame.image.load(f'Système solaire/{name}')    
        img2 =pygame.image.load(f'Système solaire/{name}')
        img3 =pygame.image.load(f'Système solaire/{name}')
        img4 =pygame.image.load(f'Système solaire/{name}')
        img5 =pygame.image.load(f'Système solaire/{name}')    
        img6 =pygame.image.load(f'Système solaire/{name}')
        img7 =pygame.image.load(f'Système solaire/{name}')
        img8 =pygame.image.load(f'Système solaire/{name}')
        
        

        """
        
        
        
        pass
    def draw(self):
        screen.blit(self.image, self.rect)
        
    def move(self, x: float, y: float, x_cos, x_sin, v,name) -> None :
        if pause:
            self.v = 0
        else:
            self.v = v
        self.t += 0.1*self.v*d
        self.x = np.cos(self.t) * x_cos
        self.y = np.sin(self.t) * x_sin
		
        self.rect.center = (self.middle_screen[0]+self.x, self.middle_screen[1]+self.y)
        self.name = name
        if name == 'C':

            self.a = self.rect.center
            pos_terre = self.a
            return pos_terre
    
            Soleil.lune(self,self.a[0], self.a[1],1)
            

    def clicked(self, mouse_pos: tuple=(0, 0)):
        mouse = pygame.mouse.get_pos()

        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="A":
            print(self.name)
            ecran.ecriture("A")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="B":
            print(self.name)
            ecran.ecriture("B")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="C":
            print(self.name)
            ecran.ecriture("C")       
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="D":
            print(self.name)
            ecran.ecriture("D")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="E":
            print(self.name)
            ecran.ecriture("E")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="F":
            print(self.name)
            ecran.ecriture("F")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="G":
            print(self.name)
            ecran.ecriture("G")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="H":
            print(self.name)
            ecran.ecriture("H")

        
def texte_presentation():
    little_screen.fill(white)


#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
 
    
class missil():

    def __init__(self, scale,x,y):
        pygame.sprite.Sprite.__init__(self)
        img =pygame.image.load('/Users/matthis/Desktop/Missile-PNG-Pic.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.y = pos_terre[1]+200
        
    def draw(self):
        screen.blit(self.image,(pos_terre[0],pos_terre[1]+200))
        
    def move(self):
        
        self.y =self.y+1
        self.rect.center = (pos_terre[0],self.y )
        
        
        
start_img = pygame.image.load('Système Solaire/Unknown.png').convert_alpha()
exit_img = pygame.image.load('Système Solaire/Unknown copie.png').convert_alpha()
pause_img = pygame.image.load('Système Solaire/Unknown-2.png').convert_alpha()
play_img = pygame.image.load('Système Solaire/Unknown-3.png').convert_alpha()

signeAstro_img = pygame.image.load('/Users/matthis/Desktop/Système Solaire/signe.jpg').convert_alpha()
signeCHinois_img = pygame.image.load('/Users/matthis/Desktop/Système Solaire/signe_chinois.jpg').convert_alpha()

#create button instances
start_button = Button(220, 700, start_img, 0.5)
exit_button = Button(10, 700, exit_img, 0.5)
pause_button = Button(80, 700, pause_img, 0.5)
play_button = Button(150, 700, play_img, 0.5)
signe_asto = Button(300, 700, signeAstro_img, 0.015)
signe_chin = Button(400, 700, signeCHinois_img, 0.09)

soleil = Soleil(1300/2, 800/2, 0.2,'S.jpeg')
mercure = Soleil(400, 320, 0.03,'mercure.jpg')
Venus = Soleil(500, 400, 0.04, 'Venus.jpg' )
terre = Soleil(600, 480, 0.04, 'Terre.jpg')
mars = Soleil(700, 560, 0.04, 'Mars.jpg')
Jupiter = Soleil(700, 560, 0.09, 'Jupiter.jpg')
saturne = Soleil(700, 560, 0.08, 'Saturne.jpg')
uranus = Soleil(700, 560, 0.19, 'uranus.jpeg')
neptune = Soleil(700, 560, 0.25, 'neptune.jpeg')
lune  = Soleil(650, 400, 0.02,'lune.jpg')
missile = missil(0.15, 900, 400)

my_sprite = TestSprite()
my_group = pygame.sprite.Group(my_sprite)


dessin = False
astres = [soleil, mercure, Venus, terre, mars, Jupiter, saturne, uranus, neptune]
pause_l =True 
ecran = ecran()
run = True
signe = False
i=0
color_active_2 = pygame.Color('lightskyblue3')
active_2 = False
input_rect_2 = pygame.Rect(80, 350, 140, 50)
color_passive_2 = pygame.Color('chartreuse4')
color = color_passive_2
user_text_2 = ''

color_active_3 = pygame.Color('lightskyblue3')
active_3 = False
input_rect_3 = pygame.Rect(80, 350, 140, 50)
color_passive_3 = pygame.Color('chartreuse4')
color = color_passive_3
user_text_3 = ''
draw = False

def find_key(user_text_2,dict_O): 
    for k, val in dict_O.items():
        for val in val:
            if val == user_text_2 :
                
                dessine_text(f'Vous êtes : {k}', font,BG, 40,490)
                
                if dict_O == dict_astro:
                
                    img_a = pygame.image.load(f'/Users/matthis/Desktop/Système Solaire/signe_astro/{k}.png')
                    img_a = pygame.transform.scale(img_a, (150, 120))
                    screen.blit(img_a, (100,530))
                if dict_O == astro_chinois:
                    
                    img_b = pygame.image.load(f'/Users/matthis/Desktop/Système Solaire/signe_chinois/{k}.jpg')
                    img_b = pygame.transform.scale(img_b, (120, 140))
                    screen.blit(img_b, (100,530))


dict_astro = {'Bélier': ['21:03','22:03','23:03','24:03','25:03','26:03','27:03','28:03','29:03','30:03','01:04','02:04','03:04','04:04','05:04','06:04','07:04','08:04','09:04','10:04','11:04','12:04','13:04','14:04','15:04','16:04','17:04','18:04','19:04','20:04'],
              'Taureau':['21:04','22:04','23:04','24:04','25:04','26:04','27:04','28:04','29:04','30:04','01:05','02:05','03:05','04:05','05:05','06:05','07:05','08:05','09:05','10:05','11:05','12:05','13:05','14:05','15:05','16:05','17:05','18:05','19:05','20:05'],
              'Gémaux':['21:05','22:05','23:05','24:05','25:05','26:05','27:05','28:05','29:05','30:05','01:06','02:06','03:06','04:06','05:06','06:06','07:06','08:06','09:06','10:06','11:06','12:06','13:06','14:06','15:06','16:06','17:06','18:06','19:06','20:06'],
              'Cancer':['21:06','22:06','23:06','24:06','25:06','26:06','27:06','28:06','29:06','30:06','01:07','02:07','03:07','04:07','05:07','06:07','07:07','08:07','09:07','10:07','11:07','12:07','13:07','14:07','15:07','16:07','17:07','18:07','19:07','20:07'],
              'Lion':['21:07','22:07','23:07','24:07','25:07','26:07','27:07','28:07','29:07','30:07','01:08','02:08','03:08','04:08','05:08','06:08','07:08','08:08','09:08','10:08','11:08','12:08','13:08','14:08','15:08','16:08','17:08','18:08','19:08','20:08'],
              'Vierge':['21:08','22:08','23:08','24:08','25:08','26:08','27:08','28:08','29:08','30:08','01:09','02:09','03:09','04:09','05:09','06:09','07:09','08:09','09:09','10:09','11:09','12:09','13:09','14:09','15:09','16:09','17:09','18:09','19:09','20:09'],
              'Balance':['21:09','22:09','23:09','24:09','25:09','26:09','27:09','28:09','29:09','30:09','01:10','02:10','03:10','04:10','05:10','06:10','07:10','08:10','09:10','10:10','11:10','12:10','13:10','14:10','15:10','16:10','17:10','18:10','19:10','20:10'],
              'Scorpion':['21:10','22:10','23:10','24:10','25:10','26:10','27:10','28:10','29:10','30:10','01:11','02:11','03:11','04:11','05:11','06:11','07:11','08:11','09:11','10:11','11:11','12:11','13:11','14:11','15:11','16:11','17:11','18:11','19:11','20:11'],
              'Sagittaire':['21:11','22:11','23:11','24:11','25:11','26:11','27:11','28:11','29:11','30:11','01:12','02:12','03:12','04:12','05:12','06:12','07:12','08:12','09:12','10:12','11:12','12:12','13:12','14:12','15:12','16:12','17:12','18:12','19:12','20:12'],
              'Capricorne':['21:12','22:12','23:12','24:12','25:12','26:12','27:12','28:12','29:12','30:12','01:01','02:01','03:01','04:01','05:01','06:01','07:01','08:01','09:01','10:01','11:01','12:01','13:01','14:01','15:01','16:01','17:01','18:01','19:01','20:01'],
              'Verseau':['21:01','22:01','23:01','24:01','25:01','26:01','27:01','28:01','29:01','30:01','01:02','02:02','03:02','04:02','05:02','06:02','07:02','08:02','09:02','10:02','11:02','12:02','13:02','14:02','15:02','16:02','17:02','18:02','19:02','20:02'],
              'Poisson':['21:01','22:01','23:01','24:01','25:01','26:01','27:01','28:01','29:01','30:01','01:03','02:03','03:03','04:03','05:03','06:03','07:03','08:03','09:03','10:03','11:03','12:03','13:03','14:03','15:03','16:03','17:03','18:03','19:03','20:03']    
              
              }
astro_chinois = {'Rat' : ['1984''1996', '2008', '2020'],
                 'Boeuf': ['1985','1997', '2009','2021'],
                 'Tigre' : ['1986','1998','2010','2022'],
                 'Liévre' : ['1987','1999','2011','2023'],
                 'Dragon' : ['1988','2000','2012','2024'],
                 'Serpent' : ['1989','2001','2013','2025'],
                 'Cheval': ['1990','2002','2014','2026'],
                 'Chévre':['1991','2003','2015','2027'],
                 'Singe' : ['1992','2004','2016','2028'],
                 'Coq': ['1993','2005','2017','2029'],
                 'Chien' : ['1994''2006', '2018', '2030'],
                 'Cochon': ['1995','2007', '2019', '2031']        
    
    }

chin = False






music = pygame.mixer.Sound("/Users/matthis/Desktop/musiques.mp3")
music.set_volume(0.05)

while run:
    

    draw_bg()
    music.play()
    
    if start_button.draw(screen):
        d = d+1
    if exit_button.draw(screen):
        d=d-1
    if pause_button.draw(screen):
        pause= True
        pause_l = False
    if play_button.draw(screen):
        pause= False
        pause_l = True
    if signe_asto.draw(screen):
        
        signe = not signe
        
    if signe == True:       
        pygame.draw.rect(screen, white, ((30, 300), (250, 350)))
        dessine_text('Savoir votre signe du ', font,BG, 50, 410)
        dessine_text('zodiaque', font,BG, 50, 430)
        
    if signe_chin.draw(screen):
        
        chin = not chin
        
        
    if chin == True:
        pygame.draw.rect(screen, white, ((30, 300), (250, 380)))
        dessine_text('Savoir votre signe', font,BG, 50, 410)
        dessine_text('astrologique chinois', font,BG, 50, 430)

    for astre in astres:
        astre.draw()
        astre.clicked()
        
    lune.draw()
    dessine_text('Entrez une date pour', font, BG, 1320, 700)
    dessine_text('connaitre les phases ', font, BG, 1320, 750)
    dessine_text('Phase de la lune', font,(255,255,255), 30, 230)
    mercure.clicked()
    ecran.page_lune()    
    mercure.move(1, 1, 80, 40,0.6,'A')
    Venus.move(1,1, 140,90,1.6,'B')
    pos_terre = terre.move(1,1, 190, 130,1.2,'C')
    mars.move(1, 1, 250, 170,0.9,'D')
    Jupiter.move(1,1,350,250,0.4,'E')
    saturne.move(1,1,430, 340,0.3,'F')
    uranus.move(1,1, 500, 420,0.2,'G')
    neptune.move(1,1 , 530, 450,0.1,'H')
    lune.lune(1, 1, 2.5, pos_terre)

    time.sleep(0.05)
    

        
    

    
    
    for event in pygame.event.get():
		#quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_b:
                ecran.ecriture("B")
            if event.key == pygame.K_c:
                ecran.ecriture("C")
            if event.key == pygame.K_d:
                ecran.ecriture("D")               
            if event.key == pygame.K_e:
                ecran.ecriture("E")
            if event.key == pygame.K_f:
                ecran.ecriture("F")
            if event.key == pygame.K_g:
                ecran.ecriture("G")             
            if event.key == pygame.K_h:
                ecran.ecriture("H")
            if event.key == pygame.K_l:
                ecran.page_lune()

                
                
            if event.key == pygame.K_p:
                pause = not pause
                pause_l = not pause_l
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            if input_rect_2.collidepoint(event.pos):
                active_2 = True
            else:
                active_2 = False
            if input_rect_3.collidepoint(event.pos):
                active_3 = True
            else:
                active_3 = False
                
        if event.type == pygame.KEYDOWN:
  
            if event.key == pygame.K_BACKSPACE:

                user_text = user_text[:-1]
                user_text_2 = user_text_2[:-1]
                
                user_text_3 = user_text_3[:-1]


            else:
                user_text += event.unicode
                user_text_2 += event.unicode
                user_text_3 += event.unicode
        
        if da.get(user_text):
            draw = True
          
        if draw:
            screen.blit(pygame.image.load(da.get(user_text)), (1320,400))
            if da.get(user_text) == Nouvellelune:
                dessine_text('pourcentage : 0%', font,BG, 1320, 500)
            if da.get(user_text) == Pleinelune:
                dessine_text('pourcentage : 100%', font,BG, 1320, 500)   
            if da.get(user_text) == lune_croissante:
                dessine_text('pourcentage : 27%', font,BG,1320, 500)
            if da.get(user_text) == premier_quartier:
                dessine_text('pourcentage : 51%', font,BG, 1320, 500)
            if da.get(user_text) == lune_decroissant:
                dessine_text('pourcentage : 26% ', font,BG, 1320, 500)      
            if da.get(user_text) == dernier_quartier:
                dessine_text('pourcentage : 50%', font,BG,1320, 500)    
  
  
    if active:
        color = color_active
    else:
        color = color_passive
    if active_2:
        color = color_active_2
    else:
        color = color_passive_2

    if active_3:
        color = color_active_3
    else:
        color = color_passive_3
        
    if pause_l == True:
        my_group.update()
        my_sprite.uptade_pourcentage()
        my_group.draw(screen)
    else:
        my_group.draw(screen)
        my_sprite.uptade_pourcentage()

    if signe == True:
        pygame.draw.rect(screen, color, input_rect_2)
        text_surface_2 = base_font.render(user_text_2, True, (255, 255, 255))
        screen.blit(text_surface_2, (input_rect_2.x+5, input_rect_2.y+5))
        input_rect_2.w = max(100, text_surface_2.get_width()+10)
        find_key(user_text_2,dict_astro)

    
    if chin == True:
        pygame.draw.rect(screen, color, input_rect_3)
        text_surface_3 = base_font.render(user_text_3, True, (255, 255, 255))
        screen.blit(text_surface_3, (input_rect_3.x+5, input_rect_3.y+5))
        input_rect_3.w = max(100, text_surface_3.get_width()+10)
        find_key(user_text_3,astro_chinois)
        
        
    
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(200, text_surface.get_width()+10)
    pygame.display.flip()        
    pygame.display.update()

pygame.quit()
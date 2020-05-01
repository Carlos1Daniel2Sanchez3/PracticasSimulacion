import pygame
import random

#COLOR = (26,150,120)
r1 = random.randrange(0,255)
r2 = random.randrange(0,255)
r3 = random.randrange(0,255)

class Rectangulo():

	def __init__(self):
		vida = random.randrange(1,3)
		self.x = 0
		self.y = 0
		self.width = random.randrange(3,10)
		self.heigth = self.width
		self.move_x = random.randrange(-3,5)
		self.move_y = random.randrange(-3,5)
		self.color= (r1, r2, r3)
		self.vida = vida

	def mover(self):
		self.x += self.move_x
		self.y += self.move_y
	
	def draw(self, pantalla):
		pygame.draw.rect(pantalla, self.color, [self.x, self.y, self.width, self.heigth])
		
	


FONDO = (0,0,0)
cantidad_de_particulas = 50

def crearParticulas(x,y):
	particulasLista = []

	for i in range (cantidad_de_particulas):
		particula= Rectangulo()
		particula.x=x
		particula.y=y
		
		particulasLista.append(particula)
	return particulasLista	

pygame.init()
pantalla = pygame.display.set_mode([700,700])
pygame.display.set_caption("Simulacion de Particulas")
FPS=60
reloj = pygame.time.Clock()

sub_lista = []

while True:
	r1 = random.randrange(0,255)
	r2 = random.randrange(0,255)
	r3 = random.randrange(0,255)
	for evento in pygame.event.get():
		if evento.type== pygame.QUIT:
			break

		elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

			x,y = evento.pos
			lista = crearParticulas(x,y)
			sub_lista.append(lista)

	pantalla.fill(FONDO)
	for lista in sub_lista:
		cont=0
		for particula in lista:
			particula.draw(pantalla)
			particula.mover()
			particula.vida -= (1.0/FPS)
			if particula.vida <= 0:
				lista.pop(cont)
			cont += 1


	pygame.display.flip()
	reloj.tick(FPS)

pygame.quit()
			


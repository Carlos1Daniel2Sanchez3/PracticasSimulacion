import pygame

NEGRO = (10, 8 ,12)
BLANCO = (255, 255, 255)
VERDE = (90, 232, 64)
ROJO = (255, 20, 20)
AZUL = (10, 222, 255)

def dibujarPistaVertical():
    pygame.draw.rect(pantalla, NEGRO, [160, 0, 160, 620])
    for i in range(10, 610, 20):
        pygame.draw.rect(pantalla, BLANCO, [234, i, 6, 8])

def dibujarPistaHorizontal():
    pygame.draw.rect(pantalla, NEGRO, [0, 160, 620, 160])
    for i in range(10, 620, 20):
        pygame.draw.rect(pantalla, BLANCO, [i, 234, 8, 6])

pygame.init()

dimensiones = [620, 480]
#dimensiones = [480, 620]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Animaciones")

hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
		hecho = True
    pantalla.fill(VERDE)
    dibujarPistaVertical()
#    dibujarPistaHorizontal()
    pygame.display.flip()
    reloj.tick(20)

pygame.quit()

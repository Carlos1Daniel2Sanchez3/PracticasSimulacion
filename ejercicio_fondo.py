
import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 920

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("peluqueria")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("salon.png")
    pel = pygame.image.load("peluquero.png").convert_alpha()

    pel_pos_x = 400
    pel_pos_y = 200

    # Indicamos la posicion de las "Surface" sobre la ventana
    #screen.blit(tux, (tux_pos_x, tux_pos_y))
    screen.blit(fondo, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:
        # le restamos 1 a la coordenada x de tux y comprobamos
        # que no alcance el borde de la pantalla
        pel_pos_x = pel_pos_x - 1
        if pel_pos_x < 1:
            pel_pos_x = 550

        # Redibujamos todos los elementos de la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(pel, (pel_pos_x, pel_pos_y))
        # se muestran lo cambios en pantalla
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()

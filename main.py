import pygame
pygame.init()

# CONSTANTES
ANCHO, ALTO = 500, 500
FPS = 30
COLOR_FONDO = (67, 129, 230)
COLOR_CARTAS = (242, 237, 73)
COLOR_BORDE = (80, 3, 148)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()
screen.fill(COLOR_FONDO)

# CLASE PADRE
class Area():
    def __init__(self, x, y, w, h, color=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def update_color(self, new_color):
        self.color = new_color

    def fill(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def border(self, border_color, border_width):
        pygame.draw.rect(screen, border_color, self.rect, border_width)


class Label(Area):
    def set_text(self, text, text_size=14, text_color=BLACK):
        self.image = pygame.font.SysFont('verdana', text_size).render(text, 1, text_color)

    def draw(self, dist_x=10, dist_y=10):
        self.fill()
        screen.blit(self.image, (self.rect.x + dist_x, self.rect.y + dist_y))

# CREANDO OBJETOS
x = 50 # valor inicial para la coordenada x
cards = [] # lista que almacena los objetos *cartas/tarjetas

# Ciclo para crear las cartas e ingresarlas en la lista
for i in range(4):
    card = Label(x, 150, 80, 100, COLOR_CARTAS)
    card.set_text('CLICK!')
    cards.append(card)
    x += 110

while True:
    # recorremos la lista de tarjetas y las dibujamos en pantalla
    for card in cards:
        card.border(COLOR_BORDE, 8)
        card.draw(15, 35)

    pygame.display.update()
    reloj.tick(FPS)

pygame.quit()


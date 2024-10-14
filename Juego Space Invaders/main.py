import pygame
import random

# Inicializar pygame
pygame.init()
pygame.mixer.init()

# Cargar recursos
fondo = pygame.image.load('imagenes/fondo.png')
laser_sonido = pygame.mixer.Sound('laser.wav')
explosion_sonido = pygame.mixer.Sound('explosion.wav')
golpe_sonido = pygame.mixer.Sound('golpe.wav')

explosion_list = [pygame.image.load(f'explosion/{i}.png') for i in range(1, 13)]

width = fondo.get_width()
height = fondo.get_height()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego Space Invaders")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Variables de estado
run = True
fps = 60
clock = pygame.time.Clock()
score = 0
vida = 100
game_over = False
pause = False


def texto_puntuacion(frame, text, size, x, y):
    font = pygame.font.SysFont('Small Fonts', size, bold=True)
    text_frame = font.render(text, True, blanco, negro)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (x, y)
    frame.blit(text_frame, text_rect)

def barra_vida(frame, x, y, nivel):
    longitud = 100
    alto = 20
    fill = int((nivel / 100 * longitud))
    border = pygame.Rect(x, y, longitud, alto)
    fill_rect = pygame.Rect(x, y, fill, alto)
    pygame.draw.rect(frame, (255, 0, 55), fill_rect)
    pygame.draw.rect(frame, negro, border, 4)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/A1.png').convert_alpha()
        pygame.display.set_icon(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height - 50
        self.velocidad_x = 0
        self.vida = 100

    def update(self):
        self.velocidad_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.velocidad_x = -5
        elif keystate[pygame.K_RIGHT]:
            self.velocidad_x = 5

        self.rect.x += self.velocidad_x
        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.left < 0:
            self.rect.left = 0

    def disparar(self):
        bala = Balas(self.rect.centerx, self.rect.top)
        grupo_jugador.add(bala)
        grupo_balas_jugador.add(bala)
        laser_sonido.play()

class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/E1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, width - 50)
        self.rect.y = random.randrange(10, 100)
        self.velocidad_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.y >= height:  # Si el enemigo sale de la pantalla, reaparece arriba
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(1, width - 50)

class Balas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('imagenes/B2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.velocidad_y = -18

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = explosion_list[0]
        img_scala = pygame.transform.scale(self.image, (20, 20))
        self.rect = img_scala.get_rect()
        self.rect.center = position
        self.time = pygame.time.get_ticks()
        self.velocidad_explo = 30
        self.frames = 0

    def update(self):
        tiempo = pygame.time.get_ticks()
        if tiempo - self.time > self.velocidad_explo:
            self.time = tiempo
            self.frames += 1
            if self.frames >= len(explosion_list):
                self.kill()  # Destruir la explosión al finalizar
            else:
                position = self.rect.center
                self.image = explosion_list[self.frames]
                self.rect = self.image.get_rect()
                self.rect.center = position

# Grupos de sprites
grupo_jugador = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas_jugador = pygame.sprite.Group()
grupo_explosiones = pygame.sprite.Group()  # Nuevo grupo para explosiones

player = Jugador()
grupo_jugador.add(player)

# Agregar enemigos al grupo
for _ in range(10):
    enemigo = Enemigos()
    grupo_enemigos.add(enemigo)

# Menús
def mostrar_menu_principal():
    menu_abierto = True
    while menu_abierto:
        window.fill(negro)
        texto_puntuacion(window, "MENU PRINCIPAL", 50, width // 2, height // 4)
        texto_puntuacion(window, "Presiona ENTER para iniciar", 30, width // 2, height // 2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_abierto = False

def mostrar_pausa():
    texto_puntuacion(window, "PAUSA", 50, width // 2, height // 4)
    texto_puntuacion(window, "Presiona P para continuar", 30, width // 2, height // 2)
    pygame.display.flip()

def mostrar_game_over():
    game_over_pantalla = True
    while game_over_pantalla:
        window.fill(negro)
        texto_puntuacion(window, "GAME OVER", 50, width // 2, height // 4)
        texto_puntuacion(window, f"Score final: {score}", 30, width // 2, height // 2)
        texto_puntuacion(window, "Presiona ENTER para reiniciar", 30, width // 2, height - 100)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Reiniciar juego

# Bucle principal
mostrar_menu_principal()

while run:
    if not game_over and not pause:
        clock.tick(fps)
        window.blit(fondo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.disparar()
                if event.key == pygame.K_p:
                    pause = True

        grupo_jugador.update()
        grupo_enemigos.update()
        grupo_balas_jugador.update()
        grupo_explosiones.update()  # Actualizar explosiones

        grupo_jugador.draw(window)
        grupo_enemigos.draw(window)
        grupo_balas_jugador.draw(window)
        grupo_explosiones.draw(window)  # Dibujar explosiones

        colision1 = pygame.sprite.groupcollide(grupo_enemigos, grupo_balas_jugador, True, True)
        for enemigo in colision1:
            score += 10
            nuevo_enemigo = Enemigos()
            grupo_enemigos.add(nuevo_enemigo)

            # Agregar explosión al grupo de explosiones
            explo = Explosion(enemigo.rect.center)
            grupo_explosiones.add(explo)
            explosion_sonido.set_volume(0.3)
            explosion_sonido.play()

        texto_puntuacion(window, f'SCORE: {score}', 30, width - 85, 2)
        barra_vida(window, width - 285, 0, player.vida)

        pygame.display.flip()

    if pause:
        mostrar_pausa()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = False

    if game_over:
        mostrar_game_over()
        game_over = False
        score = 0
        player.vida = 100
        grupo_enemigos.empty()
        grupo_explosiones.empty()
        for _ in range(10):
            enemigo = Enemigos()
            grupo_enemigos.add(enemigo)

pygame.quit()

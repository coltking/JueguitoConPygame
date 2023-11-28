import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva los círculos")

# Definir el reloj
clock = pygame.time.Clock()

# Definir la velocidad del cuadrado
SQUARE_SPEED = 5

# Definir la velocidad de los círculos
CIRCLE_SPEED = 3

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, tamaño, x, y):
    fuente = pygame.font.Font(None, tamaño)
    texto_renderizado = fuente.render(texto, True, WHITE)
    screen.blit(texto_renderizado, (x, y))

# Función principal del juego
def juego():
    # Posición inicial del cuadrado
    square_x, square_y = WIDTH // 2, HEIGHT // 2

    # Velocidad inicial del cuadrado
    square_dx, square_dy = 0, 0

    # Lista para almacenar las posiciones de los círculos
    circles = []

    # Puntuación
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Manejar la entrada del teclado para mover el cuadrado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    square_dy = -SQUARE_SPEED
                elif event.key == pygame.K_s:
                    square_dy = SQUARE_SPEED
                elif event.key == pygame.K_a:
                    square_dx = -SQUARE_SPEED
                elif event.key == pygame.K_d:
                    square_dx = SQUARE_SPEED
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    square_dy = 0
                elif event.key in (pygame.K_a, pygame.K_d):
                    square_dx = 0

        # Mover el cuadrado
        square_x += square_dx
        square_y += square_dy

        # Generar nuevos círculos aleatorios
        if random.randint(1, 100) < 5:
            circle = {'x': random.randint(0, WIDTH), 'y': random.randint(0, HEIGHT), 'dx': random.uniform(-CIRCLE_SPEED, CIRCLE_SPEED), 'dy': random.uniform(-CIRCLE_SPEED, CIRCLE_SPEED)}
            circles.append(circle)

        # Mover los círculos y manejar colisiones
        for circle in circles:
            circle['x'] += circle['dx']
            circle['y'] += circle['dy']

            # Verificar colisión con el cuadrado
            if (
                square_x < circle['x'] < square_x + 20
                and square_y < circle['y'] < square_y + 20
            ):
                mostrar_game_over(score)
                return

            # Rebote en los límites de la ventana
            if circle['x'] < 0 or circle['x'] > WIDTH:
                circle['dx'] = -circle['dx']
            if circle['y'] < 0 or circle['y'] > HEIGHT:
                circle['dy'] = -circle['dy']

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar el cuadrado
        pygame.draw.rect(screen, WHITE, (square_x, square_y, 20, 20))

        # Dibujar los círculos
        for circle in circles:
            pygame.draw.circle(screen, RED, (int(circle['x']), int(circle['y'])), 10)

        # Mostrar la puntuación
        mostrar_texto(f"Puntuación: {score}", 30, 10, 10)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(60)

        # Incrementar la puntuación
        score += 1

# Función para mostrar el menú de pausa
def mostrar_pausa():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                return

        screen.fill(BLACK)
        mostrar_texto("Juego en pausa", 50, WIDTH // 2 - 150, HEIGHT // 2 - 50)
        mostrar_texto("Presiona 'P' para continuar", 30, WIDTH // 2 - 200, HEIGHT // 2 + 50)

        pygame.display.flip()
        clock.tick(60)

# Función para mostrar el menú de game over
def mostrar_game_over(score):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

        screen.fill(BLACK)
        mostrar_texto("¡Game Over!", 50, WIDTH // 2 - 150, HEIGHT // 2 - 50)
        mostrar_texto(f"Puntuación: {score}", 30, WIDTH // 2 - 100, HEIGHT // 2 + 50)
        mostrar_texto("Presiona Enter para jugar de nuevo", 30, WIDTH // 2 - 250, HEIGHT // 2 + 100)

        pygame.display.flip()
        clock.tick(60)

# Función para mostrar el menú principal
def mostrar_menu_principal():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

        screen.fill(BLACK)
        mostrar_texto("Esquiva los círculos", 50, WIDTH // 2 - 200, HEIGHT // 2 - 50)
        mostrar_texto("Presiona Enter para empezar", 30, WIDTH // 2 - 200, HEIGHT // 2 + 50)

        pygame.display.flip()
        clock.tick(60)

# Bucle principal del juego
mostrar_menu_principal()
while True:
    juego()
    mostrar_game_over(0)

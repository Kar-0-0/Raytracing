import pygame

WIDTH = 1280
HEIGHT = 900

running = True

dragging = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

source_color = (255, 255, 255)
source_center = (200, 200)
source_radius = 150

def draw_circle(surface, color, center, radius, width=0):
    pygame.draw.circle(screen, color, center, radius, width)
    pygame.display.update()

def main():
    global running

    while running: 
        draw_circle(screen, source_color, source_center, source_radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw_circle(screen, source_color, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), source_radius)

    pygame.quit()

main()
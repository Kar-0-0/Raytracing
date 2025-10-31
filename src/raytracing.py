import pygame
import math

WIDTH = 1280
HEIGHT = 900

running = True

start = True

dragging = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

source_color = (255, 255, 255)
source_center = (200, 200)
source_radius = 75

fill_color = (0, 0, 0)

curr_xy = source_center

obj_x, obj_y = 900, 600
obj_radius = 120

num_rays = 500

def draw_circle(surface, color, center, radius, width=0):
    pygame.draw.circle(surface, color, center, radius, width)
    pygame.display.update()


def check_ray_col(rect_x, rect_y):
    if math.sqrt((rect_x-obj_x)**2 + (rect_y - obj_y)**2) < obj_radius:
        return True
    return False


def draw_rays(circ_center, num_rays, ray_color):
    ray_start_x, ray_start_y = circ_center[0], circ_center[1]
    angle_step = 360 / num_rays
    angle = 0
    
    curr_x = circ_center[0]
    curr_y = circ_center[1]

    for i in range(num_rays):
        curr_x = circ_center[0]
        curr_y = circ_center[1]

        while curr_x >= 0 and curr_x <= WIDTH and curr_y >= 0 and curr_y <= HEIGHT:
            print(angle)
            rect_x = curr_x + math.cos((angle * math.pi) / 180)
            rect_y = (curr_y + math.sin((angle * math.pi) / 180))
            
            curr_x = rect_x
            curr_y = rect_y
            
            if check_ray_col(rect_x, rect_y):
                break

            pygame.draw.rect(screen, ray_color, (rect_x, rect_y, 1, 1))


        angle += angle_step


def main():
    global running, start

    while running: 
        draw_circle(screen, (255, 255, 255), (obj_x, obj_y), obj_radius)

        if start:
            prev_mouse_x = 200
            prev_mouse_y = 200
            draw_circle(screen, source_color, source_center, source_radius)

        draw_rays((prev_mouse_x, prev_mouse_y), num_rays, source_color)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw_rays((prev_mouse_x, prev_mouse_y), num_rays, fill_color)
                start = False

                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

                draw_circle(screen, fill_color, (prev_mouse_x, prev_mouse_y), source_radius) # fill previous circle black 

                if mouse_y - source_radius < 0:
                    draw_circle(screen, source_color, (mouse_x, mouse_y + source_radius), source_radius) # draw new circle where mouse is 
                    prev_mouse_x = mouse_x
                    prev_mouse_y = mouse_y + source_radius

                elif mouse_y + source_radius > HEIGHT:
                    draw_circle(screen, source_color, (mouse_x, mouse_y - source_radius), source_radius) # draw new circle where mouse is 
                    prev_mouse_x = mouse_x
                    prev_mouse_y = mouse_y - source_radius

                elif mouse_x - source_radius < 0:
                    draw_circle(screen, source_color, (mouse_x + source_radius, mouse_y), source_radius) # draw new circle where mouse is 
                    prev_mouse_x = mouse_x + source_radius
                    prev_mouse_y = mouse_y
                
                elif mouse_x + source_radius > WIDTH:
                    draw_circle(screen, source_color, (mouse_x - source_radius, mouse_y), source_radius) # draw new circle where mouse is 
                    prev_mouse_x = mouse_x - source_radius
                    prev_mouse_y = mouse_y
                else:
                    draw_circle(screen, source_color, (mouse_x, mouse_y), source_radius) # draw new circle where mouse is 
                    prev_mouse_x = mouse_x
                    prev_mouse_y = mouse_y

    
                
                

    pygame.quit()

main()
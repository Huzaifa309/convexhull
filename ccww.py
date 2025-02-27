import pygame
import time
from button import Button


def ccw(p1, p2, p3):
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) > (p2[1] - p1[1]) * (p3[0] - p1[0])


def do_intersect(p1, q1, p2, q2):
    return ccw(p1, p2, q2) != ccw(q1, p2, q2) and ccw(p1, q1, p2) != ccw(p1, q1, q2)

points = []
dne = True

def check_intersection():
    start = time.perf_counter()
    result = do_intersect(points[0],points[1],points[2],points[3])
    end = time.perf_counter()
    execution_time = end - start
    print(f"Execution time: {execution_time:.6f} seconds")
    return result


pygame.init()

# PYGAME gui initialization
width = 800
height = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
FONT = pygame.font.Font(None, 30)

# Create buttons
reset_button = Button(None, (width - 120, height - 50), "Reset", FONT, base_color="#d7fcd4", hovering_color="White")

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('CCW ALGORITHM')

# Displaying points on the Pygame window
running = True

answer = None
checkFlag = False


while running:
    screen.fill('White')

    checkFlag = False
    # Update and draw buttons
    reset_button.update(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(points) < 4:
                x, y = pygame.mouse.get_pos()
                points.append((x, y))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            checkFlag = True
         # Handling mouse clicks for buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.checkForInput(event.pos):
                # Reset logic here (clear points, etc.)
                points = []
                answer = None
                
    for i, point in enumerate(points):
        pygame.draw.circle(screen, RED, point, 4)
        text_surface = FONT.render(str(i + 1), True, BLACK)
        screen.blit(text_surface, (point[0] + 5, point[1] - 15))

    if len(points) >= 2:
        pygame.draw.line(screen, BLACK, points[0], points[1], 2)
    if len(points) == 4:
        pygame.draw.line(screen, BLACK, points[2], points[3], 2)

        if checkFlag:
            if check_intersection():
                answer = FONT.render("Lines are intersecting!",True,GREEN)
                time_c = FONT.render("The time complexity is O(1)",True,BLACK)
                space_c = FONT.render("The space complexity is constant: O(1)",True,BLACK)
            else:
                answer = FONT.render("Lines are not intersecting!",True,RED)
                time_c = FONT.render("The time complexity is O(1)",True,BLACK)
                space_c = FONT.render("The space complexity is constant: O(1)",True,BLACK)
    if answer is not None:
        screen.blit(answer,(20,height - 90))
        screen.blit(time_c,(20,height - 70))
        screen.blit(space_c,(20,height - 50))
    

    pygame.display.update()

pygame.quit()


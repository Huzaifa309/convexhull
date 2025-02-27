import pygame
import time
from button import Button

def do_intersect(p1, q1, p2, q2):
    x_diff = (p1[0] - q1[0], p2[0] - q2[0])
    y_diff = (p1[1] - q1[1], p2[1] - q2[1])

    div = x_diff[0] * y_diff[1] - x_diff[1] * y_diff[0]
    if div == 0:
        return False  # Lines are parallel

    d = (p1[0] * q1[1] - p1[1] * q1[0], p2[0] * q2[1] - p2[1] * q2[0])
    x = (d[0] * x_diff[1] - d[1] * x_diff[0]) / div
    y = (d[0] * y_diff[1] - d[1] * y_diff[0]) / div

    if (
        min(p1[0], q1[0]) <= x <= max(p1[0], q1[0])
        and min(p2[0], q2[0]) <= x <= max(p2[0], q2[0])
        and min(p1[1], q1[1]) <= y <= max(p1[1], q1[1])
        and min(p2[1], q2[1]) <= y <= max(p2[1], q2[1])
    ):
        return True  # Intersection point lies within line segments

    return False  # Intersection point is outside line segments


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
pygame.display.set_caption('LINE INTERSECTION ALGORITHM')

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


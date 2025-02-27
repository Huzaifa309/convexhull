import pygame
import time
from button import Button


def do_intersect():
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        return 1 if val > 0 else 2  # Clockwise or Counterclockwise

    def on_segment(p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    p1, q1, p2, q2 = points

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return 1  # Segments intersect

    # Special Cases
    if (o1 == 0 and on_segment(p1, p2, q1)) or (o2 == 0 and on_segment(p1, q2, q1)) \
            or (o3 == 0 and on_segment(p2, p1, q2)) or (o4 == 0 and on_segment(p2, q1, q2)):
        return 1  # Segments intersect

    return 0  # Segments do not intersect


points = []
dne = True

def check_intersection():
    start = time.perf_counter()
    result = do_intersect()
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
pygame.display.set_caption('LINE SWEEP ALGORITHM')

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


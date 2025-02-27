import pygame
import time
import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

def convex_hull_jarvis(points):
    n = len(points)
    if n < 3:
        return points

    hull = []

    leftmost = 0
    for i in range(1, n):
        if points[i][0] < points[leftmost][0]:
            leftmost = i

    p = leftmost
    while True:
        hull.append(points[p])

        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == leftmost:
            break

    return hull

def form_hull(points):
    start = time.perf_counter()
    result = convex_hull_jarvis(points)
    end = time.perf_counter()
    execution_time = end - start
    print(f"Execution time: {execution_time:.6f} seconds")
    return result

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JARVIS MARCH CONVEX HULL ALGORITHM")

answer = None
running = True
points = []
hull_points = []

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hull_points:  # Clear points and hull if a hull already exists
                points = []
                hull_points = []
            x, y = pygame.mouse.get_pos()
            points.append((x, y))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                hull_points = form_hull(points)
                
    time_c = FONT.render("The time complexity is O(n^2) worst case, O(nh) in average case",True,BLACK)
    space_c = FONT.render("The space complexity is O(n) it stores input and output points",True,BLACK)
    
    for i, point in enumerate(points):
        pygame.draw.circle(screen, RED, point, 4)
        text_surface = FONT.render(str(i + 1), True, BLACK)
        screen.blit(text_surface, (point[0] + 5, point[1] - 15))

    if len(hull_points) > 1:
        pygame.draw.polygon(screen, BLACK, hull_points, 2)
        screen.blit(time_c,(20,HEIGHT - 70))
        screen.blit(space_c,(20,HEIGHT - 50))
    pygame.display.flip()

pygame.quit()

import pygame
import math
import time

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

def convex_hull_graham_scan(points):
    n = len(points)
    if n < 3:
        return points

    # Find the point with the lowest y-coordinate (and leftmost in case of a tie)
    min_point = min(points, key=lambda x: (x[1], x[0]))

    # Sort the points based on polar angle with respect to the min_point
    points.sort(key=lambda x: (math.atan2(x[1] - min_point[1], x[0] - min_point[0]), -x[1], x[0]))

    hull = [points[0], points[1]]
    
    for i in range(2, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])

    return hull

def form_hull(points):
    start = time.perf_counter()
    result = convex_hull_graham_scan(points)
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
pygame.display.set_caption("GRAHAM SCAN CONVEX HULL ALGORITHM")

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
                
    time_c = FONT.render("It performs O(nlogn) operations",True,BLACK)
    space_c = FONT.render("The space complexity is  O(n) as it stores input and output points",True,BLACK)
    
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

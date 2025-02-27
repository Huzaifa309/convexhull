import pygame
import math
import time

def findSide(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])

    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def lineDist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

def quickHull(a):
    def quickHullUtil(a, p1, p2, side, hull):
        ind = -1
        max_dist = 0

        for i in range(len(a)):
            temp = lineDist(p1, p2, a[i])

            if (findSide(p1, p2, a[i]) == side) and (temp > max_dist):
                ind = i
                max_dist = temp

        if ind == -1:
            hull.append(p1)
            hull.append(p2)
            return

        quickHullUtil([point for idx, point in enumerate(a) if idx != ind], a[ind], p1, -findSide(a[ind], p1, p2), hull)
        quickHullUtil([point for idx, point in enumerate(a) if idx != ind], a[ind], p2, -findSide(a[ind], p2, p1), hull)

    if len(a) < 3:
        return a

    hull = []
    min_x = 0
    max_x = 0
    for i in range(1, len(a)):
        if a[i][0] < a[min_x][0]:
            min_x = i
        if a[i][0] > a[max_x][0]:
            max_x = i

    quickHullUtil(a, a[min_x], a[max_x], 1, hull)
    quickHullUtil(a, a[min_x], a[max_x], -1, hull)

    return hull

def form_hull(points):
    start = time.perf_counter()
    result = quickHull(points)
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
pygame.display.set_caption("QUICK HULL/ELIMINATION ALGORITHM FOR CONVEX HULL")

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
                
    time_c = FONT.render("Its average case time complexity is O(nlogn) but in worst case O(n^2)",True,BLACK)
    space_c = FONT.render("The space complexity is  O(n) as it stores input and output points",True,BLACK)
    
    for i, point in enumerate(points):
        pygame.draw.circle(screen, RED, point, 4)
        text_surface = FONT.render(str(i + 1), True, BLACK)
        screen.blit(text_surface, (point[0] + 5, point[1] - 15))

    if len(hull_points) > 1:
        min_point = min(hull_points, key=lambda x: (x[1], x[0]))
        hull_points.sort(key=lambda x: (math.atan2(x[1] - min_point[1], x[0] - min_point[0]), -x[1], x[0]))
        pygame.draw.polygon(screen, BLACK, hull_points, 2)
        screen.blit(time_c,(20,HEIGHT - 70))
        screen.blit(space_c,(20,HEIGHT - 50))
    pygame.display.flip()

pygame.quit()

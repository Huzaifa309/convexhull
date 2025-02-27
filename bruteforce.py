import pygame
import time
import math


def convex_hull_brute_force(points):
    n = len(points)
    if n < 3:
        return points

    hull = []

    # Helper function to find orientation of three points (p, q, r)
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        return 1 if val > 0 else 2  # Clockwise or counterclockwise

    # Check all combinations of points to form potential edges
    for i in range(n):
        for j in range(n):
            valid = True

            # Check all points against the edge formed by points[i] and points[j]
            for k in range(n):
                if k != i and k != j:
                    orient = orientation(points[i], points[j], points[k])

                    # If any point lies on the left side of the edge, it's not a valid edge
                    if orient != 2:
                        valid = False
                        break

            # If the edge is valid, add its points to the hull
            if valid:
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    return hull

def form_hull():
    start = time.perf_counter()
    result = convex_hull_brute_force(points)
    end = time.perf_counter()
    execution_time = end - start
    print(f"Execution time: {execution_time:.6f} seconds")
    return result

points = []
hull_points = []

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BRUTE FORCE CONVEX HULL ALGORITHM")

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
                hull_points = form_hull()
                
    time_c = FONT.render("The time complexity turns out to be O(n^3)",True,BLACK)
    space_c = FONT.render("The space complexity is O(n)",True,BLACK)
    
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
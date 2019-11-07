###SQUARE###
# import pygame
# screen = pygame.display.set_mode((640, 480))
# running = True
# clock = pygame.time.Clock()
# s = 1
# s_dir = 1
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0, 0, 0))
#     pygame.draw.rect(screen, (0, 128, 128), ((80, 80), (s, s)))
#     pygame.display.update()
#
#     s += s_dir
#     if s == 200 or s == 1:
#         s_dir = s_dir * -1
#
#     clock.tick(60)
#
# pygame.quit()

###QUESTION 1###
# import pygame
# screen = pygame.display.set_mode((640, 480))
# running = True
# r = 0
# g = 0
# b = 0
# s = 1
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (0, g, 0), (320, 240), 90)
#     pygame.display.update()
#     g += s
#     if g >= 255 or g <= 0:
#         s = s * -1
# pygame.quit()

###QUESTION 2###
# import pygame
# screen = pygame.display.set_mode((640, 480))
# running = True
# clock = pygame.time.Clock()
# s = 1
# s_dir = 1
# a = 1
# a_dir = 2
# b = 1
# b_dir = 3
# c = 1
# c_dir = 4
# l = 1
# l_dir = 5
# r = 0
# g = 0
# b = 0
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (r % 255, g % 255, b % 255), (100, 240), s)
#     pygame.draw.circle(screen, (r % 25, 0, b % 42), (200, 240), a)
#     pygame.draw.circle(screen, (r % 80, g % 215, b % 55), (300, 240), b)
#     pygame.draw.circle(screen, (r % 2, g % 72, b % 38), (400, 240), c)
#     pygame.draw.circle(screen, (r % 18, g % 66, b % 100), (500, 240), l)
#     pygame.display.update()
#     r = r + 1
#     g = g + 1
#     b = b + 1
#
#     s += s_dir
#     if s > 50 or s <= 1:
#         s_dir = s_dir * -1
#     a += a_dir
#     if a > 50 or a <= 1:
#         a_dir = a_dir * -1
#     b += b_dir
#     if b > 50 or b <= 1:
#         b_dir = b_dir * -1
#     c += c_dir
#     if c > 50 or c <= 1:
#         c_dir = c_dir * -1
#     l += l_dir
#     if l > 50 or l <= 1:
#         l_dir = l_dir * -1
# pygame.quit()

###QUESTION 3###
import pygame
import random as random
screen = pygame.display.set_mode((640,480))

x = 0
lst = []
for x in range(30):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    lst.append([red, green, blue])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    s = 300
    for i in range(len(lst)):

        pygame.draw.circle(screen, (lst[i]), (320,240), s)
        s = s - 10
        lst[i][0] =  (lst[i][0] + 1) % 255                   #meaning of this line

    pygame.display.update()

pygame.quit()


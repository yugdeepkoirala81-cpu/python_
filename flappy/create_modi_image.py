import pygame

# Initialize pygame
pygame.init()

# Create surface
width, height = 60, 60
surface = pygame.Surface((width, height))
surface.fill((255, 255, 255))  # White background

# Colors
skin = (212, 165, 116)
hair = (26, 26, 26)
orange = (255, 140, 66)
black = (0, 0, 0)

# Draw head (circle)
pygame.draw.circle(surface, skin, (30, 20), 15)

# Draw hair (arc at top)
pygame.draw.arc(surface, hair, (15, 5, 45, 30), -3.14, 0, 5)
pygame.draw.polygon(surface, hair, [(10, 20), (15, 10), (35, 8), (50, 15), (48, 22)])

# Draw eyes
pygame.draw.circle(surface, black, (24, 17), 2)
pygame.draw.circle(surface, black, (36, 17), 2)

# Draw nose
pygame.draw.polygon(surface, (192, 144, 96), [(30, 18), (28, 24), (32, 24)])

# Draw mouth
pygame.draw.line(surface, black, (26, 26), (34, 26), 2)

# Draw body (orange kurta)
pygame.draw.rect(surface, orange, (8, 35, 44, 20))

# Draw arms
pygame.draw.rect(surface, skin, (2, 38, 6, 12))
pygame.draw.rect(surface, skin, (52, 38, 6, 12))

# Add black outline
pygame.draw.rect(surface, black, (8, 35, 44, 20), 2)

# Save image
pygame.image.save(surface, 'modi.png')
print("Modi character image created: modi.png")

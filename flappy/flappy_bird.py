import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Game variables
GRAVITY = 0.6
JUMP_STRENGTH = -8
PIPE_SPEED = -5
PIPE_WIDTH = 50
PIPE_GAP = 150
PIPE_FREQUENCY = 90  # frames between pipes

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Try to load image, fallback to generated surface
        try:
            self.image = pygame.image.load('modi.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
        except:
            # Fallback: Create Modi character with orange and text if image not found
            self.image = pygame.Surface((50, 50))
            self.image.fill(ORANGE)
            font = pygame.font.Font(None, 20)
            text = font.render("MODI", True, WHITE)
            text_rect = text.get_rect(center=(25, 25))
            self.image.blit(text, text_rect)
        
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0
        self.alive = True

    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        
        # Check bounds
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.alive = False

    def jump(self):
        self.velocity = JUMP_STRENGTH


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, gap_y):
        super().__init__()
        # Top pipe
        self.top_image = pygame.Surface((PIPE_WIDTH, gap_y))
        self.top_image.fill(GREEN)
        
        # Bottom pipe
        self.bottom_y = gap_y + PIPE_GAP
        self.bottom_image = pygame.Surface((PIPE_WIDTH, SCREEN_HEIGHT - self.bottom_y))
        self.bottom_image.fill(GREEN)
        
        self.rect = self.top_image.get_rect(topleft=(x, 0))
        self.x = x
        self.gap_y = gap_y
        self.scored = False

    def update(self):
        self.x += PIPE_SPEED
        self.rect.x = self.x
        
        # Remove if off screen
        if self.x + PIPE_WIDTH < 0:
            self.kill()

    def draw(self, screen):
        # Draw top pipe
        screen.blit(self.top_image, (self.x, 0))
        # Draw bottom pipe
        screen.blit(self.bottom_image, (self.x, self.bottom_y))

    def collides_with(self, bird):
        # Check if bird hits top or bottom pipe
        bird_rect = bird.rect
        
        # Top pipe collision
        if bird_rect.left < self.x + PIPE_WIDTH and bird_rect.right > self.x:
            if bird_rect.top < self.gap_y:
                return True
        
        # Bottom pipe collision
        if bird_rect.left < self.x + PIPE_WIDTH and bird_rect.right > self.x:
            if bird_rect.bottom > self.bottom_y:
                return True
        
        return False

    def check_score(self, bird):
        # Award point when bird passes pipe
        if not self.scored and bird.rect.centerx > self.x + PIPE_WIDTH:
            self.scored = True
            return True
        return False


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Modi - PM of India")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    # Create bird
    bird = Bird(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
    
    # Sprite groups
    pipes = pygame.sprite.Group()
    
    # Game variables
    score = 0
    game_over = False
    pipe_counter = 0
    
    # Main game loop
    running = True
    while running:
        clock.tick(60)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if not game_over:
                        bird.jump()
                    else:
                        # Restart game
                        bird = Bird(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
                        pipes.empty()
                        score = 0
                        game_over = False
                        pipe_counter = 0
        
        if not game_over:
            # Update bird
            bird.update()
            
            # Generate pipes
            pipe_counter += 1
            if pipe_counter > PIPE_FREQUENCY:
                gap_y = random.randint(80, SCREEN_HEIGHT - PIPE_GAP - 80)
                new_pipe = Pipe(SCREEN_WIDTH, gap_y)
                pipes.add(new_pipe)
                pipe_counter = 0
            
            # Update pipes
            pipes.update()
            
            # Check collisions with pipes
            for pipe in pipes:
                if pipe.collides_with(bird):
                    game_over = True
                
                # Check if bird passed pipe
                if pipe.check_score(bird):
                    score += 1
            
            # Check if bird is alive
            if not bird.alive:
                game_over = True
        
        # Draw everything
        screen.fill(WHITE)
        
        # Draw pipes
        for pipe in pipes:
            pipe.draw(screen)
        
        # Draw bird
        screen.blit(bird.image, bird.rect)
        
        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if game_over:
            game_over_font = pygame.font.Font(None, 48)
            game_over_text = game_over_font.render("GAME OVER", True, RED)
            restart_text = font.render("Press SPACE to Restart", True, BLACK)
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

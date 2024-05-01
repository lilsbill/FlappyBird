import pygame
from sys import exit
import random
from menuScreen import new_menu

pygame.init()
clock = pygame.time.Clock()

menus = new_menu()

# Window
win_height = 720
win_width = 1200
window = pygame.display.set_mode((win_width, win_height))

#bird1 = pygame.image.load("image/fish.png")
#bird2 = pygame.image.load("image/fish_up.png")
#bird3 = pygame.image.load("image/fish_down.png")

bird1 = pygame.image.load("image/fishy.png")
bird2 = pygame.image.load("image/fishy.png")
bird3 = pygame.image.load("image/fishy.png")

image_size = (100, 70)
#image_size = (50, 50)

bird1 = pygame.transform.scale(bird1, image_size)
bird2 = pygame.transform.scale(bird2, image_size)
bird3 = pygame.transform.scale(bird3, image_size)

skyline = pygame.image.load("image/background.jpeg")
skyline_image = pygame.transform.scale(skyline, (win_width, win_height))

# Images
bird_images = [bird1, bird2, bird3]
#skyline_image = pygame.image.load("image/background.jpeg")
ground_image = pygame.image.load("images/ground.png")
#top_pipe_image = pygame.image.load("images/pipe_top.png")
#bottom_pipe_image = pygame.image.load("images/pipe_bottom.png")

#top_pipe_image = pygame.image.load("image/coral_top.png")
#bottom_pipe_image = pygame.image.load("image/coral_bottom.png")

pipe_width = 200
pipe_height = 800



pipe_coral_top = pygame.image.load("pipe/pipes_top.png")
pipe_coral_bottom = pygame.image.load("pipe/pipes_btm.png")
game_over_image = pygame.image.load("images/game_over.png")
start_image = pygame.image.load("images/start.png")
#extra_pipe_top = pygame.image.load("image/pipe_top.png")
#extra_pipe_bottom = pygame.image.load("image/pipe_bottom.png")
pipe_bottom_blue = pygame.image.load("pipes/pipe_b_blue.png")
pipe_top_blue = pygame.image.load("pipes/pipe_t_blue.png")


pipe_bottom_orange = pygame.image.load("pipes/pipe_b_orange.png")
pipe_top_orange = pygame.image.load("pipes/pipe_t_orange.png")
pipe_bottom_yellow = pygame.image.load("pipes/pipe_b_yellow.png")
pipe_top_yellow = pygame.image.load("pipes/pipe_t_yellow.png")


extra_pipe_top = pygame.image.load("pipe/seaweed_top.png")
extra_pipe_bottom = pygame.image.load("pipe/seaweed_btm.png")

bubble_top = pygame.image.load("pipe/bubble_top.png")
bubble_btm = pygame.image.load("pipe/bubble_btm.png")

bubble_top = pygame.transform.scale(bubble_top, (150, 400))
bubble_btm = pygame.transform.scale(bubble_btm, (150, 400))

clam_open = pygame.image.load("pipe/clam_open.png")
clam_closed = pygame.image.load("pipe/clam_closed.png")

clam_open = pygame.transform.scale(clam_open, (250, 250))
clam_closed = pygame.transform.scale(clam_closed, (250, 250))



top_pipe_image = pygame.transform.scale(pipe_coral_top, (pipe_width, pipe_height))
bottom_pipe_image = pygame.transform.scale(pipe_coral_bottom, (pipe_width, pipe_height))
extra_pipe_top = pygame.transform.scale(extra_pipe_top, (100,400))
extra_pipe_bottom = pygame.transform.scale(extra_pipe_bottom, (100,400))
pipe_bottom_blue = pygame.transform.scale(pipe_bottom_blue, (pipe_width, pipe_height))
pipe_top_blue = pygame.transform.scale(pipe_top_blue, (pipe_width, pipe_height))
pipe_bottom_orange = pygame.transform.scale(pipe_bottom_orange, (pipe_width, pipe_height))
pipe_top_orange = pygame.transform.scale(pipe_top_orange, (pipe_width, pipe_height))
pipe_bottom_yellow = pygame.transform.scale(pipe_bottom_yellow, (pipe_width, pipe_height))
pipe_top_yellow = pygame.transform.scale(pipe_top_yellow, (pipe_width, pipe_height))



# Game
scroll_speed = 3
bird_start_position = (300, 250)
score = 0
font = pygame.font.SysFont('Segoe', 50)
game_stopped = True


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0
        self.vel = 0
        self.flap_strength = -4
        self.gravity = 0.1
        self.flap = False
        self.alive = True

    def update(self, user_input):
        # Animate Bird
        if self.alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]

        # Gravity and Flap
        #gravity = .3

        #self.vel += gravity
        #if self.vel > 7:
        #    self.vel = 7
        #if self.rect.y < 500:
        #    self.rect.y += int(self.vel)
        #if self.vel == 0:
        #    self.flap = False

        if self.alive:
            self.vel += self.gravity  # Apply gravity
            if self.flap:  # If flapping, counteract gravity with flap_strength
                self.vel = self.flap_strength
                self.flap = False
            self.rect.y += int(self.vel)

        # Rotate Bird
        self.image = pygame.transform.rotate(self.image, self.vel * -7)
        #self.image = pygame.transform.scale(self.image, (50,50))


        # User Input
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            #self.vel = -4


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type, pipe_kind):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type
        self.pipe_kind = pipe_kind

    def update(self):
        # Move Pipe
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()

        # Score
        global score
        if self.pipe_type == 'bottom':
            if bird_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if bird_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()


def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Menu
def main():
    global score
    global scroll_speed

    # Instantiate Bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    # Setup Pipes
    pipe_timer = 0
    pipes = pygame.sprite.Group()

    # Instantiate Initial Ground
    GROUND_WIDTH = 551
    ground = pygame.sprite.Group()
    for i in range(win_width // GROUND_WIDTH + 2):
        ground.add(Ground(i * GROUND_WIDTH, win_height - ground_image.get_height()))

    run = True
    while run:
        # Quit
        quit_game()

        # Reset Frame
        window.fill((0, 0, 0))

        # User Input
        user_input = pygame.key.get_pressed()

        # Draw Background
        window.blit(skyline_image, (0,0))

        # Spawn Ground
        last_ground = ground.sprites()[-1]
        if last_ground.rect.right <= win_width:
            ground.add(Ground(last_ground.rect.right, win_height - ground_image.get_height()))

        # Draw - Pipes, Ground and Bird
        pipes.draw(window)
        ground.draw(window)
        bird.draw(window)

        bird_rect_debug = pygame.Rect(bird.sprites()[0].rect)
        bird_rect_debug.inflate_ip(-2, -2)
        pygame.draw.rect(window, (255, 0, 0), bird_rect_debug, 2)
        for pipe in pipes:
            pipe_rect_debug = pygame.Rect(pipe.rect)
            pipe_rect_debug.inflate_ip(-2, -2)
            pygame.draw.rect(window, (0, 255, 0), pipe_rect_debug, 2)

        # Show Score
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20))

        # Update - Pipes, Ground and Bird
        if bird.sprite.alive:
            pipes.update()
            ground.update()
        bird.update(user_input)

        # Collision Detection
        bird_rect = bird.sprites()[0].rect
        for pipe in pipes:
            if pipe.pipe_kind == 1:

                if bird_rect.colliderect(pipe.rect):
                    bird.sprite.alive = False
                    break

            if pipe.pipe_kind == 2:
                if bird_rect.colliderect(pipe.rect):
                    bird.sprites()[0].rect.x -= 40
                    #scroll_speed = scroll_speed + 1
                    #bird.sprite.alive = False
                    #break
                #scroll_speed = scroll_speed + 1
            
            if pipe.pipe_kind == 3:
                if bird_rect.colliderect(pipe.rect):
                    #bird.sprites()[0].rect.y += 20

                    if pipe.pipe_type == "top":
                        bird.sprites()[0].rect.y += 40
                    elif pipe.pipe_type == "bottom":
                        bird.sprites()[0].rect.y -= 40

            if pipe.pipe_kind == 4:
                if bird_rect.colliderect(pipe.rect):
                    bird.sprites()[0].vel = 0
                    
                
            
        # Collision with ground
        collision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if collision_ground:
            bird.sprite.alive = False

        # Handle game over
        if not bird.sprite.alive:
            window.blit(game_over_image, (win_width // 2 - game_over_image.get_width() // 2,
                                          win_height // 2 - game_over_image.get_height() // 2))
            pygame.display.update()
            if user_input[pygame.K_r]:
                score = 0
                main()
            else:
                break

        # Spawn Pipes
        if pipe_timer <= 0 and bird.sprite.alive:
            #x_top, x_bottom = 1200, 1200
            #y_top = random.randint(-800, -480)
            #y_bottom = y_top + random.randint(200, 250) + bottom_pipe_image.get_height()
            
            if score < 5:
                random_value = random.randint(4, 4)
            elif score < 10:
                random_value = random.randint(4, 4)
            elif score < 15:
                random_value = random.randint(4, 4)

            pipe_kind = random_value

            if random_value == 1:
                x_top, x_bottom = 1200, 1200
                y_top = random.randint(-800, -520)
                y_bottom = y_top + random.randint(200, 250) + bottom_pipe_image.get_height()

                pipes.add(Pipe(x_top, y_top, top_pipe_image, 'top', 1))
                pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom', 1))


            elif random_value == 2:
                pipe_num = random.randint(1, 2)

                x_top, x_bottom = 1200, 1200

                if pipe_num == 1:
                    y_top = random.randint(-200, -30)
                    pipes.add(Pipe(x_top, y_top, extra_pipe_top, 'top', 2))
                else:
                    y_bottom = random.randint(100, 300)
                    pipes.add(Pipe(x_bottom, y_bottom, extra_pipe_bottom, 'bottom', 2))
                #y_top = random.randint(-100, -20)
                #y_bottom = y_top + random.randint(200, 250) + bottom_pipe_image.get_height()

                #pipes.add(Pipe(x_top, y_top, extra_pipe_top, 'top', 2))
                #pipes.add(Pipe(x_bottom, y_bottom, extra_pipe_bottom, 'bottom', 2))

            elif random_value == 3:
                pipe_num = random.randint(1, 2)

                x_top, x_bottom = 1200, 1200

                if pipe_num == 1:
                    y_top = random.randint(-200, -30)
                    pipes.add(Pipe(x_top, y_top, bubble_top, 'top', 3))
                else:
                    y_bottom = random.randint(100, 300)
                    pipes.add(Pipe(x_bottom, y_bottom, bubble_btm, 'bottom', 3))


            elif random_value == 4:
                x_top, x_bottom = 1200, 1200
                y_bottom = random.randint(100, 300)

                #pipes.add(Pipe(x_top, y_top, pipe_top_orange, 'top', 4))
                pipes.add(Pipe(x_bottom, y_bottom, clam_open, 'bottom', 4))
            elif random_value == 5:
                pipes.add(Pipe(x_top, y_top, pipe_top_yellow, 'top', 5))
                pipes.add(Pipe(x_bottom, y_bottom, pipe_bottom_yellow, 'bottom', 5))

            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1

        clock.tick(60)
        pygame.display.update()


def menu():
    global game_stopped

    while game_stopped:
        quit_game()

        window.fill((0, 0, 0))
        #input_user = pygame.key.get_pressed()
        new_input = menus.run()
        if new_input == 2:
            #main()
            window.fill((0, 0, 0))
            window.blit(skyline_image, (0, 0))
            window.blit(ground_image, Ground(0, 520))
            window.blit(bird_images[0], (100, 250))
            window.blit(start_image, (win_width // 2 - start_image.get_width() // 2,
                                    win_height // 2 - start_image.get_height() // 2))

        # Draw Menu
        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()
            

        pygame.display.update()



menu()
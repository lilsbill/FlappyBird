#scaling pipes

#pipe_coral_top = pygame.image.load("image/coral_top.png")
#pipe_coral_bottom = pygame.image.load("image/coral_bottom.png")

pipe_coral_top = pygame.image.load("image/long_coral_top.png")
pipe_coral_bottom = pygame.image.load("image/long_coral_btm.png")


top_pipe_image = pygame.transform.scale(pipe_coral_top, (pipe_width, pipe_height))
bottom_pipe_image = pygame.transform.scale(pipe_coral_bottom, (pipe_width, pipe_height))


#top_pipe_image = pygame.image.load("image/coral_top.png")
#bottom_pipe_image = pygame.image.load("image/coral_bottom.png")
#

game_over_image = pygame.image.load("images/game_over.png")
start_image = pygame.image.load("images/start.png")

#

#new_pipe_top = pygame.image.load("image/pipe_top.png")
#new_pipe_bottom = pygame.image.load("image/pipe_bottom.png")

#extra_pipe_top = pygame.transform.scale(new_pipe_top, (pipe_width, pipe_height))
#extra_pipe_bottom = pygame.transform.scale(new_pipe_bottom, (pipe_width, pipe_height))

#

extra_pipe_top = pygame.image.load("image/pipe_top.png")
extra_pipe_bottom = pygame.image.load("image/pipe_bottom.png")

pipe_bottom_blue = pygame.image.load("pipes/pipe_b_blue.png")
pipe_top_blue = pygame.image.load("pipes/pipe_t_blue.png")

pipe_bottom_orange = pygame.image.load("pipes/pipe_b_orange.png")
pipe_top_orange = pygame.image.load("pipes/pipe_t_orange.png")

pipe_bottom_yellow = pygame.image.load("pipes/pipe_b_yellow.png")
pipe_top_yellow = pygame.image.load("pipes/pipe_t_yellow.png")







elif pipe.pipe_kind == 2:
                    #bird.sprites()[0].rect.x += 80
                    #scroll_speed = 4
                    #bird.sprite.alive = False
                    pass

                elif pipe.pipe_kind == 3:
                    #bird.sprites()[0].rect.x += 80
                    #scroll_speed = 5
                    #bird.sprite.alive = False
                    pass

                elif pipe.pipe_kind == 4:
                    #bird.sprites()[0].rect.x += 80
                    #scroll_speed = 6
                    #bird.sprite.alive = False
                    pass
                
                elif pipe.pipe_kind == 5:
                    #bird.sprites()[0].rect.x += 80
                    #scroll_speed = 7
                    #bird.sprite.alive = False
                    pass
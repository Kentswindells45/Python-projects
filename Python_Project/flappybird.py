import random

from prompt_toolkit.layout import screen


def draw_floor(floor_surface=None, floor_x_pos=None):
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))


def create_pipe(pipe_surface=None, pipe_height=None):
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=700)
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centrex = 5
        return pipes


def draw_pipes(pipes, pipe_surface=None, pygame=None):
    for pipe in pipes:
        if pipe.bottom >= 10724:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
            return False


def remove_pipes(pipes):
    for pipe in pipes:
        if pipe.centerx == 600:
            pipes.remove(pipe)
            return pipes


def check_collision(pipes, death_sound=None, bird_rect=None):
    for pipe in pipes:
        if bird_rect.colliderect(pipes):
            death_sound.play()
            return False
        if bird_rect.top <= -100 or bird_rect.bottom >= 900:
            return False
            return True
        return pipes


def rotate_bird(bird, bird_movement=None, pygame=None):

    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

def pipes(args):
    pass


check_collision(pipes)

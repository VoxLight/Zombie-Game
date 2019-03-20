import sys, pygame, tools
from math import sqrt
from zombie import Zombie
from player import Player


def game_loop():
    # Consts {
    RESOLUTION = SCREEN_WIDTH, SCREEN_HEIGHT = 1366, 768
    FPS = 60
    # }

    # Bools {
    alive = True
    mouse_is_down = False
    diff_up = False
    # }
    
    # Ints{
    elapsed = 0
    # }

    # Strings {
    # }

    # Lists {
    player_dest = None
    # }

    # PyGame {
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    clock = pygame.time.Clock()
    # }

    # Player {
    player = Player()
    # }


    # Enemy {
    zombies = []
    enemies = 0
    # }

    # Game_Loop
    while alive:
        # Clear the screen
        screen.fill((0, 0, 0))

        

        # Handle Input    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                alive = False
                continue
            if event.type == pygame.MOUSEBUTTONDOWN and event.__dict__['button'] == 3:
                mouse_is_down = True
            elif event.type == pygame.MOUSEBUTTONUP and event.__dict__['button'] == 3:
                mouse_is_down = False

        # Update the player, then draw them to the screen
        if mouse_is_down:
            player_dest = pygame.mouse.get_pos()
        player.update(player_dest)
        player.draw(screen)

        # Every second add a zombie
        if len(zombies) < 100:
            elapsed += clock.get_time()
            if elapsed >= 1000:
                elapsed = 0
                zombies.append(Zombie())
        elif not diff_up:
            diff_up = True
        
        # Update each zombie, then draw it to the screen
        for z in zombies:
            z.update(player.center)
            if diff_up:
                z.difficulty += 0.00001
            z.draw(screen)
            if tools.distance(z.center, player.center) <= (player.width - (z.width+(z.width/2))):
                alive = False
                continue
            
        
        

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()

import sys, pygame, tools
from math import sqrt
from zombie import Zombie
from player import Player


def game_loop():
    # Consts {
    RESOLUTION = SCREEN_WIDTH, SCREEN_HEIGHT = 1366, 768
    SCREEN_CENTER = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    FPS = 60
    # }

    # Bools {
    alive = True
    mouse_is_down = False
    diff_up = False
    # }
    
    # Ints{
    elapsed = 0
    gamemode = 3         
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
        #PyGame.font{
    font = None
    font_rect = None
    if gamemode == 3:
        while not pygame.font.get_init:
            pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 40)
        font_rect = pygame.Rect((SCREEN_CENTER), (0, 0))
        # }
    # }

    # Player {
    player = Player()
    # }


    # Enemy {
    zombies = []
    enemies = 0
    # }

    # Game {
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
        if gamemode == 1:
            zdest = player.center
        elif gamemode == 2:
            zdest = player.dest
        elif gamemode == 3:
            zdest = player.dest
            color = (255, 255, 255) if len(zombies) < 100 else (255, 0, 0)
            text = font.render(str(len(zombies)), True, color)
            screen.blit(text, font_rect)
        else:
            zdest = player.center
        for z in zombies:
            z.update(zdest)
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

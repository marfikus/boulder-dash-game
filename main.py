
from map import Map
from player import Player
from stone import Stone
from ground import Ground
from diamond import Diamond


def start_console():
    map = Map()
    player = Player("Nick")
    map.add_player(player)
    # map.add_stone(Stone(), 0, 3)
    map.add_random_object("stone", nums=5, diff=2)
    map.add_random_object("diamond", nums=5, diff=2)
    map.add_ground()
    
    # map.map[0][4].content = None

    map.show()
        
    while True:
        result = None
        com = input()
        if com == "q":
            break
        elif com == "s":
            result = player.move("left")
        elif com == "f":
            result = player.move("right")
        elif com == "e":
            result = player.move("up")
        elif com == "d":
            result = player.move("down")
        # map.show()
        if result == False:
            break


def start_gui():
    import pygame

    MAP_WIDTH = 10
    MAP_HEIGHT = 10

    map = Map(MAP_WIDTH, MAP_HEIGHT)
    player = Player("Nick")
    map.add_player(player)
    # map.add_stone(Stone(), 0, 3)
    map.add_random_object("stone", nums=5, diff=2)
    map.add_random_object("diamond", nums=5, diff=2)
    map.add_ground()
    # map.map[0][4].content = None
    map.show()

    BLOCK_SIZE = 20
    SCREEN_WIDTH = MAP_WIDTH * BLOCK_SIZE
    SCREEN_HEIGHT = MAP_HEIGHT * BLOCK_SIZE
    FPS = 60
    GAME_SPEED = 500

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    # GAME_STATE_FILENAME = "game_state"

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Boulder Dash")
    clock = pygame.time.Clock()
    TIMEREVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMEREVENT, GAME_SPEED)


    def update_screen():
        screen.fill(BLACK)
        x = 0
        y = 0
        for h in range(MAP_HEIGHT):
            for w in range(MAP_WIDTH):
                if map.map[h][w].player_here:
                    pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
                    # continue
                content = map.map[h][w].content
                if content is not None:
                    if isinstance(content, Stone):
                        pygame.draw.rect(screen, RED, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
                    elif isinstance(content, Diamond):
                        pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
                    elif isinstance(content, Ground):
                        pygame.draw.rect(screen, GREEN, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))

                x += BLOCK_SIZE
            x = 0
            y += BLOCK_SIZE
        pygame.display.update()


    running = True
    is_need_update_screen = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                is_need_update_screen = True

                result = None
                if event.key == pygame.K_LEFT:
                    result = player.move("left")
                elif event.key == pygame.K_RIGHT:
                    result = player.move("right")
                elif event.key == pygame.K_UP:
                    result = player.move("up")
                elif event.key == pygame.K_DOWN:
                    result = player.move("down")
                elif event.key == pygame.K_q:
                    running = False

                if result == False:
                    running = False

        if is_need_update_screen:
            update_screen()
            is_need_update_screen = False

        clock.tick(FPS)
    pygame.quit()


def main():
    cmd = input("Select version please (1 - console, 2 - gui): ")
    # cmd = "1"
    if cmd == "1":
        start_console()
    elif cmd == "2":
        start_gui()
    else:
        print("Unknown command!")


if __name__ == "__main__":
    main()



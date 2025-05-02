
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
    pass


def main():
    # cmd = input("Select version please (1 - console, 2 - gui): ")
    cmd = "1"
    if cmd == "1":
        start_console()
    elif cmd == "2":
        start_gui()
    else:
        print("Unknown command!")


if __name__ == "__main__":
    main()



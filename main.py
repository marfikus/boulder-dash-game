
from map import Map
from player import Player
from stone import Stone
from ground import Ground
from diamond import Diamond


def main():
    map = Map()
    player = Player("Nick")
    map.add_player(player)
    map.map[0][1].content = Ground()
    map.map[0][2].content = Diamond()
    map.map[4][7].content = Diamond()
    map.map[7][3].content = Diamond()
    map.map[5][5].content = Diamond()
    map.map[9][9].content = Diamond()
    map.add_stone(Stone(), 0, 3)
    map.add_stone(Stone(), 0, 9)
    map.add_stone(Stone(), 1, 3)
    map.add_stone(Stone(), 2, 5)
    map.add_stone(Stone(), 4, 6)
    map.add_stone(Stone(), 5, 1)
    map.add_ground()
    # map.show()
    map.map[0][4].content = None
    map.map[0][5].content = None
    map.map[0][6].content = None
    map.map[0][7].content = None
    map.map[0][8].content = None

    # map.map[2][4].content = None
    # map.map[3][4].content = None
    # map.map[4][4].content = None
    # map.map[2][6].content = None
    # map.map[3][6].content = None
    # map.map[4][6].content = None


    map.show()

    # for s in map.stones:
    #     print((s.y, s.x))

    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("right")
    # player.move("down")
    # player.move("down")
    # player.move("down")
    # player.move("left")
    # player.move("left")
    # player.move("up")
    # player.move("left")
    # player.move("left")
    # player.move("up")
    # player.move("up")
    # player.move("left")

    # stone = Stone()
    # map.add_stone(stone, 9, 2)
    # map.show()
    # map.remove_stone(stone)
    # map.show()

    # for s in map.stones:
    #     print((s.y, s.x))
        
        
    while True:
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


if __name__ == "__main__":
    main()

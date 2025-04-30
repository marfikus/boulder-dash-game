
import random

from cell import Cell
from stone import Stone
from ground import Ground
from diamond import Diamond


class Map:
    def __init__(self, w=10, h=10):
        self.width = w
        self.height = h
        self.map = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.player = None
        self.diamonds = []
        self.stones = []


    def show(self):
        border = " " + "-=-" * len(self.map[0])
        print(border)
        for y in range(self.height):
            print("|", end="")
            num_line = " "
            for x in range(self.width):
                num_line += f" {x} "
                if self.map[y][x].player_here:
                    print(" p ", end="")
                    continue
                content = self.map[y][x].content
                if content is None:
                    print("   ", end="")
                elif isinstance(content, Stone):
                    print(" s ", end="")
                elif isinstance(content, Diamond):
                    print(" d ", end="")
                elif isinstance(content, Ground):
                    print(" g ", end="")
            print("|", y)
        print(border)
        print(num_line)
        
        
    def add_player(self, p):
        if self.player is not None:
            return
        
        self.player = p
        self.map[p.y][p.x].player_here = True
        p.map_link = self
        
        
    def remove_player(self, p):
        if p == self.player:
            p.map_link = None
            self.player = None
            self.map[p.y][p.x].player_here = False
            
            
    def add_ground(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x].player_here:
                    continue
                content = self.map[y][x].content
                if content is None:
                    self.map[y][x].content = Ground()
    
    
    def add_stone(self, stone, y, x):
        if stone in self.stones:
            return
        
        # по идее надо проверять координаты, не занята ли ячейка..
        self.map[y][x].content = stone
        
        self.stones.append(stone)
        stone.y = y
        stone.x = x

    
    def remove_stone(self, stone):
        if stone not in self.stones:
            return
        
        self.map[stone.y][stone.x].content = None
        
        self.stones.remove(stone)
        stone.y = None
        stone.x = None


    def add_diamond(self, diamond, y, x):
        if diamond in self.diamonds:
            return
        
        # по идее надо проверять координаты, не занята ли ячейка..
        self.map[y][x].content = diamond
        
        self.diamonds.append(diamond)
        diamond.y = y
        diamond.x = x

    
    def remove_diamond(self, diamond):
        if diamond not in self.diamonds:
            return
        
        self.map[diamond.y][diamond.x].content = None
        
        self.diamonds.remove(diamond)
        diamond.y = None
        diamond.x = None
    
    
    def update_map(self) -> bool:
        # проверяем карту, выполняем падение камней, алмазов...
        def check_side_cells(y, x):
            left_side = [(y, x - 1), (y + 1, x - 1)]
            right_side = [(y, x + 1), (y + 1, x + 1)]
            result = []
            
            # много повторов, можно сократить..
            
            if (left_side[0][1] >= 0) and (left_side[1][0] < self.height):
                y1 = left_side[0][0]
                x1 = left_side[0][1]
                content_1 = self.map[y1][x1].content
                player_not_here1 = not self.map[y1][x1].player_here
                y2 = left_side[1][0]
                x2 = left_side[1][1]
                content_2 = self.map[y2][x2].content
                player_not_here2 = not self.map[y2][x2].player_here
                if (content_1 is None) and (content_2 is None) and player_not_here1 and player_not_here2:
                    result.append(left_side)
            
            if (right_side[0][1] < self.width) and (right_side[1][0] < self.height):
                y1 = right_side[0][0]
                x1 = right_side[0][1]
                content_1 = self.map[y1][x1].content
                player_not_here1 = not self.map[y1][x1].player_here
                y2 = right_side[1][0]
                x2 = right_side[1][1]
                content_2 = self.map[y2][x2].content
                player_not_here2 = not self.map[y2][x2].player_here
                if (content_1 is None) and (content_2 is None) and player_not_here1 and player_not_here2:
                    result.append(right_side)
            
            return result
        
        
        diffs = True
        while diffs:
            diffs = False
            for stone in self.stones:
                stone_steps = 0
                while True:
                    new_y = stone.y + 1
                    new_x = stone.x
                    if new_y == self.height:
                        break
    
                    if self.map[new_y][new_x].player_here:
                        # тут еще возможен вариант, когда камень уже летит и падает на игрока...
                        if stone_steps >= 2:
                            print("Game over!")
                            # в этом случае можно перемещать камень на место игрока, типа его прихлопнуло)
                            return False
                        break
                        
                    # проверка возможности срыва(скатывания) камня
                    content_under_stone = self.map[new_y][new_x].content
                    if content_under_stone is not None:
                        available_rockfalls = check_side_cells(stone.y, stone.x)
                        # if available_rockfalls["available"]:
                        if len(available_rockfalls) > 0:
                            print("available rockfalls", available_rockfalls)
                            # определяем: скатываться или нет
                            falling = random.choice([True, False])
                            if falling:
                                # выбираем направление
                                side = random.choice(available_rockfalls)
                                print(side)
                                new_x = side[0][1]
                            else:
                                break
                        else:
                            break
    
                    # move stone:
                    self.map[new_y][new_x].content = stone
                    self.map[stone.y][stone.x].content = None
                    stone.y = new_y
                    stone.x = new_x
                    stone_steps += 1
                    diffs = True
        return True


from stone import Stone
from ground import Ground
from diamond import Diamond


class Player:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.level = 1
        self.map_link = None
        self.diamonds = 0
        

    def move(self, new_dir) -> bool:
        def check_on_borders(map, y, x):
            if (y < 0) or (y == len(map)):
                return False
            if (x < 0) or (x == len(map[0])):
                return False
            
            return True
        
        dirs = {
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
            "up": (-1, 0),
        }
        
        print(new_dir)
        map = self.map_link.map
        new_y = self.y + dirs[new_dir][0]
        new_x = self.x + dirs[new_dir][1]
        
        if not check_on_borders(map, new_y, new_x):
            print("Border!")
            return

        if isinstance(map[new_y][new_x].content, Ground):
            self.map_link.map[new_y][new_x].content = None
        elif isinstance(map[new_y][new_x].content, Diamond):
            self.map_link.map[new_y][new_x].content = None
            self.diamonds += 1
            print("Diamonds:", self.diamonds)
        elif isinstance(map[new_y][new_x].content, Stone):
            if self.y != new_y:
                print("This stone cannot be moved(up/down)!")
                return
            
            after_stone_y = new_y + dirs[new_dir][0]
            after_stone_x = new_x + dirs[new_dir][1]
            if not check_on_borders(map, after_stone_y, after_stone_x):
                print("Border after stone!")
                return
            
            content_after_stone = map[after_stone_y][after_stone_x].content
            if content_after_stone is not None:
                print("This stone cannot be moved(busy cell after)!")
                return
            
            # move stone:
            stone = self.map_link.map[new_y][new_x].content
            stone.y = after_stone_y
            stone.x = after_stone_x
            self.map_link.map[after_stone_y][after_stone_x].content = stone
            self.map_link.map[new_y][new_x].content = None
            print("stone moved:", (stone.y, stone.x))
        
        self.map_link.map[self.y][self.x].player_here = False
        self.y = new_y
        self.x = new_x
        self.map_link.map[new_y][new_x].player_here = True
        
        result = self.map_link.update_map()
        
        self.map_link.show()
        return result

import time

class ConwaysGame():
    def __init__(self):
        self.map = [[]]
        self.width = 0
        self.height = 0

    def set_world_size(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for i in range(height)] for i in range(width)]

    def populate(self, x, y):
        self.map[x][y] = 1

    def cell_is_alive(self, x, y):
        return self.map[x][y] == 1

    def number_of_live_neighbours(self, x, y):
        live_neighbours = 0
        for i in range(max(x - 1, 0), min(x + 1, self.width - 1) + 1):
            for j in range (max(y - 1, 0), min(y + 1, self.height - 1) + 1):
                if self.cell_is_alive(i, j) == True and (i == x and j == y) == False:
                    live_neighbours += 1
        return live_neighbours

    def step(self):
        # 1. Any live cell with < 2 live neighbour dies
        # 2. Any live cell 2 or 3 live neighbours will live
        # 3. Any live cell with > 3 live neighbours dies
        # 4. Any dead cell with exactly three live neighbours comes to life
        new_map = [[0 for i in range(self.height)] for i in range(self.width)]
        for x in range(0, self.width):
            for y in range(0, self.height):
                # 1
                if self.number_of_live_neighbours(x, y) < 2:
                    new_map[x][y] = 0
                # 2
                if self.cell_is_alive(x, y) == True and \
                   (self.number_of_live_neighbours(x, y) == 2 or \
                   self.number_of_live_neighbours(x, y) == 3):
                    new_map[x][y] = 1
                # 3
                if self.cell_is_alive(x, y) == True and \
                   self.number_of_live_neighbours(x, y) > 3:
                    new_map[x][y] = 0
                # 4
                if self.cell_is_alive(x, y) == False and \
                   self.number_of_live_neighbours(x, y) == 3:
                    new_map[x][y] = 1

        self.map = new_map

        return

    def __str__(self):
        grid_string = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.cell_is_alive(x, y):
                    grid_string += "◼"
                else:
                    grid_string += "◻"
            if y < self.height - 1:
                grid_string += "\n"

        return grid_string

if __name__ == '__main__':
    # Let's make a glider
    game = ConwaysGame()
    game.set_world_size(20, 20)
    game.populate(2, 1)
    game.populate(3, 2)
    game.populate(1, 3)
    game.populate(2, 3)
    game.populate(3, 3)

    while True:
        print(game)
        print("-" * 20)
        game.step()
        time.sleep(0.5)


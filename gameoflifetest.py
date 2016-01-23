import unittest

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
        # 3. Any live cll with > 3 live neighbours dies
        # 4. Any dead cell with exactly three live neighbours comes to life
        new_map = [[0 for i in range(self.height)] for i in range(self.width)]
        for x in range(0, self.width):
            for y in range(0, self.height):
                # 1
                if self.number_of_live_neighbours(x, y) < 2:
                    new_map[x][y] = 0
                # 4
                if self.cell_is_alive(x, y) == False and \
                   self.number_of_live_neighbours(x, y) == 3:
                    new_map[x][y] = 1

        self.map = new_map

        return

class ConwaysGameTests(unittest.TestCase):
    def test_set_world_size(self):
        '''set_world_size should set the width and height of the world'''
        game = ConwaysGame()
        game.set_world_size(10, 5)
        self.assertEqual(game.width, 10)
        self.assertEqual(game.height, 5)
    
    def test_populate_and_cell_is_alive(self):
        game = ConwaysGame()
        game.set_world_size(10,10)
        game.populate(1, 2)
        game.populate(7, 4)
        self.assertEqual(game.cell_is_alive(2, 2), False)
        self.assertEqual(game.cell_is_alive(1, 2), True)
        self.assertEqual(game.cell_is_alive(7, 4), True)

    def test_populate_outside_of_range(self):
        game = ConwaysGame()
        game.set_world_size(3, 1)
        self.assertRaises(IndexError, game.populate, 3, 0)
        self.assertRaises(IndexError, game.populate, 0, 1)

# OOOOO
# OOOOO
# XXOOO
# XOOOO
# OOOOO

    def test_number_of_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(5, 5)
        game.populate(0, 2)
        game.populate(0, 3)
        game.populate(1, 2)
        self.assertEqual(game.number_of_live_neighbours(1, 3), 3)
        self.assertEqual(game.number_of_live_neighbours(1, 1), 2)
        self.assertEqual(game.number_of_live_neighbours(2, 2), 1)
        self.assertEqual(game.number_of_live_neighbours(0, 0), 0)

    def test_step_two_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(2, 2)
        game.populate(0, 0)
        game.populate(1, 0)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(1, 1), False)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), False)

    def test_step_live_cell_with_two_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(3, 1)
        game.populate(0, 0)
        game.populate(1, 0)
        game.populate(2, 0)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(2, 0), True)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(2, 0), False)

    def test_step_dead_cell_with_three_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(3, 3)
        game.populate(0, 0)
        game.populate(0, 2)
        game.populate(2, 1)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), True)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), False)
        self.assertEqual(game.cell_is_alive(1, 2), False)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), True)
        self.assertEqual(game.cell_is_alive(2, 2), False)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), False)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), True)
        self.assertEqual(game.cell_is_alive(1, 2), False)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), False)
        self.assertEqual(game.cell_is_alive(2, 2), False)

#    def test_step(self):
#        game = ConwaysGame()
#        game.set_world_size(5, 5)
#        game.populate(0, 2)
#        game.populate(0, 3)
#        game.populate(1, 2)
#        self.assertEqual(game.cell_is_alive(1, 3), False)
#        self.assertEqual(game.cell_is_alive(0, 0), False)
#        self.assertEqual(game.cell_is_alive(1, 0), False)
#        self.assertEqual(game.cell_is_alive(0, 1), False)
#        self.assertEqual(game.cell_is_alive(1, 1), False)
#        game.step()
#        self.assertEqual(game.cell_is_alive(0, 2), True)
#        self.assertEqual(game.cell_is_alive(0, 3), True)
#        self.assertEqual(game.cell_is_alive(1, 2), True)
#        self.assertEqual(game.cell_is_alive(1, 3), True)
#        self.assertEqual(game.cell_is_alive(0, 0), False)
#        self.assertEqual(game.cell_is_alive(1, 0), False)
#        self.assertEqual(game.cell_is_alive(0, 1), False)
#        self.assertEqual(game.cell_is_alive(1, 1), False)


if __name__ == '__main__':
    unittest.main()


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


if __name__ == '__main__':
    unittest.main()


import unittest

class ConwaysGame():
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_world_size(self, width, height):
        self.width = width
        self.height = height


class ConwaysGameTests(unittest.TestCase):
    def test_set_world_size(self):
        '''set_world_size should set the width and height of the world'''
        game = ConwaysGame()
        game.set_world_size(10, 5)
        self.assertEqual(game.width, 10)
        self.assertEqual(game.height, 5)

if __name__ == '__main__':
    unittest.main()


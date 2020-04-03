import unittest

from game.player import Player, AI


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_build_not_enough_stone(self):
        # Should fail 
        self.player.castle = 2
        self.player.stone = 0
        self.player.build()
        self.assertEqual(self.player.castle, 2)

    def test_build_enough_stone(self):
        self.player.castle = 2
        self.player.stone = 1
        self.player.build()
        self.assertEqual(self.player.castle, 3)

    def test_gather_food(self):
        self.player.food = 1
        self.player.villagers = 1
        self.player.gather()
        self.assertEqual(self.player.food, 2)

    def test_attack(self):
        self.player.warriors = 2
        opponent = Player()
        opponent.castle = 2
        self.player.attack(opponent)
        self.assertEqual(opponent.castle, 0)


class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI()

    def test_build_enough_stone(self):
        self.ai.castle = 2
        self.ai.stone = 1
        self.ai.build()
        self.assertEqual(self.ai.castle, 3)
    
    def test_attack(self):
        self.ai.warriors = 2
        opponent = Player()
        opponent.castle = 2
        self.ai.attack(opponent)
        self.assertEqual(opponent.castle, 0)


if __name__ == '__main__':
    unittest.main()
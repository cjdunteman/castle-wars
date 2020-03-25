import os, random

class Player():
    def __init__(self):
        self.castle = 1
        self.villagers = 1
        self.warriors = 0
        self.food = 0
        self.stone = 0

    def build(self):
        if self.stone >= 1:
            self.castle += 1
            self.stone -= 1
            return False
        else:
            os.system('clear')
            if self.__class__.__name__ == "Player":
                print("You don't have enough stone!\n")
            return True

    def gather(self):
        self.food += self.villagers
        self.stone += self.villagers
        return False

    def recruit(self):
        if self.food >= 1:
            self.warriors += 1
            self.food -= 1
            return False
        else:
            os.system('clear')
            if self.__class__.__name__ == "Player":
                print("You don't have enough food!\n")
            return True

    def attack(self, opponent):
        if self.warriors >= 1:
            if self.__class__.__name__ == "Player":
                opponent.castle -= self.warriors
            elif self.__class__.__name__ == "AI":
                opponent.castle -= self.warriors


class AI(Player):
    def __init__(self):
        super().__init__()
        
    def makeMove(self, player):
        action = 0
        # Win if player castle weak
        if player.castle <= self.warriors:
            super().attack(player)
        # Build if castle weak
        elif self.castle == player.warriors:
            if self.stone >= 1:
                super().build()
        else:
            action = random.randint(1, 4)
        
        if action == 1:
            super().build()
        if action == 2:
            super().gather()
        if action == 3:
            super().recruit()
        if action == 4:
            super().attack(player)
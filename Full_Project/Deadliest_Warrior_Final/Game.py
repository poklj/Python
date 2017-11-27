import Deadliest_Warrior_Final.Person as Person
from random import randint
class Game:
    def __init__(self, Player1:Person, Player2:Person):
        """
        Setup a Game Object to Run the simulation
        :param Player1: Set Player 1 (Required) [Person]
        :param Player2: Set Player 2 (Required) [Person]
        """
        self.Player1 = Player1
        self.Player2 = Player2

    def Combat(self):
        """
        Do a Single 'Tick' of Combat
        :return: 1 if Player 1 Wins, 2 if Player 2 wins
        """
        tickRand = randint(0,1) # Grab Random 1 or 0 For combat this tick

        if tickRand == 0: # Player 1 Wins the random roll
            if (self.Player1.WieldingL.Strength + self.Player1.WieldingR.Strength) > (self.Player2.WieldingL.Defense +  self.Player2.WieldingR.Defense):
                return 1
            else:
                return 2

        elif tickRand == 1: # Player 2 Wins
            if (self.Player2.WieldingL.Strength + self.Player2.WieldingR.Strength) > (self.Player1.WieldingL.Defense +  self.Player1.WieldingR.Defense):
                return 2
            else:
                return 1
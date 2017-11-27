from Deadliest_Warrior.Sword import Sword
from Deadliest_Warrior.Fist import Fist

class Pile:
    def __init__(self, *inpile):
        self.Opile = []
        for i in inpile:
            self.Opile.append(i)
        self.Default = Fist()

    def RandomPullfrom(self):
        from random import randint
        if self.Opile:
            #return self.Opile.pop(randint(0, len(self.Opile) - 1))
            return self.Opile[randint(0, len(self.Opile) - 1)]
        else:
            return self.Default

    def PullSpecificFrom(self, x):
        return self.Opile.pop(x)

    def printself(self):
        print(self.Opile)


# a = Pile(Sword(1, 1, "The Broken One"), Sword(12, 12, "Ogawdwai"))
# print(a.RandomPullfrom())
# a.printself()

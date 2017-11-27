from Deadliest_Warrior.Person import Person
from random import randint

class Group:
    def __init__(self, *Warriors:Person):
        """
        Generate the Group Object of Warriors
        :param Warriors:
        """
        self.Warriors = []

        for i in Warriors:
            self.Warriors.append(i)

    def getGroupSize(self):
        return len(self.Warriors)

    def KillIndiv(self, Who):
        self.Warriors.remove(Who)

    def getWarrior(self, Who):
        return self.Warriors[Who]

    def RandomWarrior(self):
        return self.Warriors[
            randint(0, len(self.Warriors) - 1)
        ]

    def CheckAlive(self):
        # for i in self.Warriors:
        #     if i.Alive == 0:
        #         self.KillIndiv(i)
        dead = 0
        #print(self.Warriors)
        for i in self.Warriors:
            if i.Alive == 0:
                print(i.Alive)
                dead += 1
                break
        if dead == len(self.Warriors):
            return True

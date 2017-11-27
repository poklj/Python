from Deadliest_Warrior.Group_System import Group
from Deadliest_Warrior.PileOweapons import Pile
from random import randint


class Game:
    def __init__(self, Group1: Group, Group2: Group, Pile1: Pile, Pile2: Pile):
        """

        :param Group1: Filled Group Object
        :param Group2: Filled Group Object
        :param Pile1: Filled Pile Object
        :param Pile2: Filled Pile Object
        """
        self.Group1 = Group1

        self.Group2 = Group2
        self.Pile1 = Pile1
        self.Pile2 = Pile2

    def do_fight(self):
        """

        :return:
        """
        a = self.Group1.RandomWarrior()
        b = self.Group2.RandomWarrior()

        a.gainWeapon(
            self.Pile1.RandomPullfrom()
        )
        b.gainWeapon(
            self.Pile2.RandomPullfrom()
        )
        #c = randint(0, 1)

        # TODO: reevaluate this
        while a.Alive == 1 & b.Alive == 1:
            if randint(0, 1) == 0:
                print("B swing A")
                a.swing(b)
                if b.Alive == 1:
                    print("A swing B")
                    b.swing(a)
                else:
                    break
            else:
                print("B swing A")
                b.swing(a)
                if a.Alive == 1:
                    print("A swing B")
                    a.swing(b)
                else:
                    break
        if a.Alive == 0:
            print("Group1 Fighter Wins")
        elif b.Alive == 0:
            print("Group2 Fighter Wins")
        else:
            return

    def Groupcheck(self):
        """
        Run each Groups Check Alive Function
        :return:
        """

        a = self.Group1.CheckAlive()
        b = self.Group2.CheckAlive()


        if a and not b or b and not a or a and b:
            if not a:
                print("Group 2")
                return True
            if not b:
                print("Group 1")
                return True
            if a and b:
                return False

        else:
            print("THEY'RE ALL DEAD")


        # if self.Group2.CheckAlive():
        #     print("Group1 Wins")
        #     return True
        # elif self.Group1.CheckAlive():
        #     print("Group2 Wins")
        #     return True


    # def CheckWin(self):
    #     """
    #     Check Both Groups to see if they are alive
    #     :return: Will return 1 or 2 if none of them are alive (the numbers correspond to the two teams)
    #     """
    #     if :
    #
    #     if not self.Group2.Warriors:
    #         print("Group2 Entirely Eliminated")
    #         return 2
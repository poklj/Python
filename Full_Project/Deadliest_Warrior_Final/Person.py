import Deadliest_Warrior_Final.Weapon as Weapon


class Person:

    def __init__(self, WieldingL=None, WieldingR=None):
        """
        Set up a Person As a Fighter
        :param WieldingL: Weapon left [Weapon]
        :param WieldingR: Weapon Right [Weapon]
        """
        self.WieldingL = WieldingL
        self.WieldingR = WieldingR
        # TODO: If WieldingL + WieldingR is None, Cause the Person to ALWAYS lose

    def Grab(self, weapon:Weapon, Side:str):
        """
        Grab function to Change weapons if need be
        :param Weapon: The weapon to Equip [Weapon]
        :param Side: Side to Equip the Weapon (L or R)
        :return:
        """
        if Side.upper() == "L":
            self.WieldingL = weapon
        elif Side.upper() == "R":
            self.WieldingR = weapon
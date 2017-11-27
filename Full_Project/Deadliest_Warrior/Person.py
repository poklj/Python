import Deadliest_Warrior.Fist as Fiste

Fis = Fiste


class Person:
    def __init__(self, Wielding=None, speed=1):
        """

        :param Wielding: Object of weapon
        :param speed: How fast the Person is
        """
        if Wielding == None:
            self.Wielding = Fis
        else:
            self.Wielding = Wielding
        self.Alive = 1
        self.Speed = speed

    def _get(self):
        """
        Debug
        :return: Everything (PRINT)
        """
        print(self.Alive, self.Wielding)

    def swing(self, target):
        # TODO: gut this
        """
        Swing at a target
        :param target: Person Object to attack
        :return:
        """

        s:int = self.Wielding.get_str_()
        if s == None or s == 0 or s < 0 :
            s = 1
        if target.contestDefense(s):
            target.Kill()
        else:
            target.reduce_wep_def(s - target.get_weapon_str() + 1)

    def reduce_wep_def(self, by):
        """
        Used to reduce the Wielded weapon by X
        :param by: reduce the defense of a weapon by X
        :return:
        """
        self.Wielding.reduce_def(by)

    def get_weapon_str(self):
        """

        :return: return the Wielded weapons Strength
        """
        return self.Wielding.get_str_()

    def contestDefense(self, s: int):

        #TODO: Gut this
        """

        :param s: Strength of Opposing weapon
        :return: Does it go through (Bool)
        """
        if self.Wielding.get_def() == None or s > self.Wielding.get_def():
            return True
        else:
            return False


    def Kill(self):
        """

        :return: Make the person Drop dead
        """
        self.Alive = 0

    def getAlive(self):
        """
        Get Alive State
        :return: Boolean of Alive value (Converted)
        """
        if self.Alive == 0:
            return False
        else:
            return True

    def gainWeapon(self, Weapon):
        self.Wielding = Weapon

        # Wah = Sword.Sword(2,2,"aaaa")
        # War1 = Person()
        # War1.get()
        # ShitWah = Sword.Sword(2,2,"bbbb")
        # War2 = Person()

        # while True:
        #     if War1.Alive and War2.Alive:
        #         if War1.Speed > War2.Speed:
        #             War1.swing(War2)
        #             War2.swing(War1)
        #         else:
        #             War2.swing(War1)
        #             War1.swing(War2)
        #     else:
        #         if not War1.Alive:
        #             print("War2 Wins")
        #             break
        #         elif not War2.Alive:
        #             print("War1 Wins")
        #             break

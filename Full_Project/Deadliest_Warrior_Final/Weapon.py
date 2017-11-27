

class Weapon:

    def __init__(self, Strength:int, Defense:int):
        """
        Setup a Weapon Object Where Both Strength and Defense must be <= 5 and together be <= 7
        :param Strength: Integer of Strength <= 5
        :param Defense:  Integer of Defense <= 5
        """
        if (Strength + Defense) <= 7:
            if Strength <= 5:
                if Defense <= 5:
                    self.Strength = Strength
                    self.Defense = Defense
        else:
            raise ValueError("Total Power is over 7")
class Sword:
    def __init__(self, str_: int, def_:int, name="Sword"):
        """
        Sword is a Weapon Class used by Person
            CONSTRAINT: Str_ + def_ <= 7
        :param str_: Initial Strength of the weapon
        :param def_: Initial Defense of the weapon
        """
        self.str_:int = str_
        self.def_:int = def_

        if self.str_ + self.def_ >= 7:
            raise ValueError("Sword Generated with Out of bounds Combined Strength")

        self.name_ = name

    def get(self):
        """
        Return All values
        :return: Print
        """
        for i in self:
            print(i)

    def get_str_(self):
        """
        Get the weapon strength
        :return: Weapons Str
        """
        return self.str_

    def get_def(self):
        """
        Get Weapon defense
        :return: Weapon Defense
        """
        if self.def_ != None:
            return self.def_
        else:
            return int(0)

    def reduce_def(self, by):
        # TODO: gut this
        """
        Reduce this weapons Defense
        :param by: Amount of defense to reduce the Defense by (X)
        :return:
        """
        if self.def_ - by < 0 :
            self.def_:int = 0
        else:
            self.def_ -= by

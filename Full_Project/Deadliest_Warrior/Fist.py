from Deadliest_Warrior.Sword import Sword


class Fist(Sword):
    def __init__(self):
        """
        This is just a Blank type for fists that defaults to 1 1 fist
        """
        super().__init__(1, 1, "Fist")

    def get_def(self):
        super().get_def()

    def get_str_(self):
        super().get_str_()

    def reduce_def(self, by):
        super().reduce_def(by=by)

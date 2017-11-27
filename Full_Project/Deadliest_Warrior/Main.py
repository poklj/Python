from Deadliest_Warrior.PileOweapons import Pile
from Deadliest_Warrior.Group_System import Group
from Deadliest_Warrior.Sword import Sword
from Deadliest_Warrior.Game import Game
from Deadliest_Warrior.Person import Person

def main():

    p1 = [Sword(1,4,"Stone Sword"),Sword(2,3,"Bronze Sword"),Sword(4,1,"Glass Sword"), Sword(1,1,"Kweh")]
    p1c = Pile(*p1)
    p2c = Pile(*p1)
    g1 = [Person()]
    g1c = Group(*g1)
    g2c = Group(*g1)
    game = Game(Group1=g1c, Group2=g2c, Pile1=p1c, Pile2=p2c)

    while True:
        #g1c.Warriors[1]._get()
        # game.Groupcheck()
        while True:
            game.do_fight()
            if not game.Groupcheck():
               break


# def main():
#     p1 = Sword(2,2,"Sword")
#     p2 = Sword(2,2,"Sword")
#
#     g1 = Person(Wielding=p1)
#     g2 = Person(Wielding=p2)
#
#     while g1.Alive == 1 & g2.Alive == 1:
#         if c == 0:
#             print("A swing B")
#             a.swing(b)
#             if b.Alive == 1:
#                 print("A swing B")
#                 b.swing(a)
#             else:
#                 break
#         else:
#             print("B swing A")
#             b.swing(a)
#             if a.Alive == 1:
#                 print("A swing B")
#                 a.swing(b)
#             else:
#                 break
#     if a.Alive == 0:
#         print("Group1 Fighter Wins")
#     elif b.Alive == 0:
#         print("Group2 Fighter Wins")
#     else:
#         return

if __name__ == "__main__":
    main()
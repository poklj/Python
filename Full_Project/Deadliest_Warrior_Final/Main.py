import Deadliest_Warrior_Final.Person as Person
import Deadliest_Warrior_Final.Game as Game
import Deadliest_Warrior_Final.Weapon as Weapon

def main():
    weapon = Weapon.Weapon(2,2)
    p1 = Person.Person(WieldingL=weapon, WieldingR=weapon)
    p2 = Person.Person(WieldingL=weapon, WieldingR=weapon)

    game = Game.Game(p1, p2)

    ticks = 0
    player1Wins = 0
    player2Wins = 0
    while ticks != 500:
        a = game.Combat()
        if a == 1:
            player1Wins += 1
        elif a == 2:
            player2Wins += 1
        ticks += 1
    printOut(tick=ticks, p1Wins=player1Wins, p2Wins=player2Wins)

def printOut(p1Wins, p2Wins, tick):
    print("*********** SIMULATION FINISHED ************* \n \t Ticks: {0} \n \n \t * Player | Wins * \n \t * Player 1 | {1} * \n \t * Player 2 | {2} *".format(tick, p1Wins, p2Wins))

if __name__ == "__main__":
    main()
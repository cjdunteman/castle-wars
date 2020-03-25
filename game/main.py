import os

from game import Player, AI


def gameLoop():
    player = Player()
    ai = AI()

    # MAIN LOOP
    playing = True
    while playing:

        playerTurn = True
        while playerTurn:
            print("You:\nCastle: " + str(player.castle) + " Food: " + str(player.food) + " Stone: " + str(player.stone) + " Villagers: " + str(player.villagers) + " Warriors: " + str(player.warriors) + "\n")
            print("Computer:\nCastle: " + str(ai.castle) + " Food: " + str(ai.food) + " Stone: " + str(ai.stone) + " Villagers: " + str(ai.villagers) + " Warriors: " + str(ai.warriors) + "\n")

            action = 0
            action = int(input("1) Build\n2) Gather\n3) Recruit\n4) Attack\n"))
            if action == 1:
                playerTurn = player.build()
            elif action == 2:
                playerTurn = player.gather()
            elif action == 3:
                playerTurn = player.recruit()
            elif action == 4:
                playerTurn = player.attack(ai)
            else:
                playerTurn = True

        ai.makeMove(player)   

        if ai.castle <= 0:
            playing = False
            print("You Win!\n")
        elif player.castle <= 0:
            playing = False
            print("You Lose!")
        else:
            os.system('clear')

if __name__ == '__main__':
    gameLoop()
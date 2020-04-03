import os

from player import Player, AI

def game_loop():
    player = Player()
    ai = AI()

    # MAIN LOOP
    playing = True
    while playing:

        player_turn = True
        while player_turn:
            print(f"""You:
Castle: {player.castle}
Food: {player.food}
Stone: {player.stone}
Villagers: {player.villagers}
Warriors: {player.warriors}
""")

            print(f"""Computer:
Castle: {ai.castle}
Food: {ai.food}
Stone: {ai.stone}
Villagers: {ai.villagers}
Warriors: {ai.warriors}
""")

            action = 0
            action = int(input("1) Build\n2) Gather\n3) Recruit\n4) Attack\n"))
            if action == 1:
                player_turn = player.build()
            elif action == 2:
                player_turn = player.gather()
            elif action == 3:
                player_turn = player.recruit()
            elif action == 4:
                player_turn = player.attack(ai)
            else:
                playerTurn = True

        ai.make_move(player)   

        if ai.castle <= 0:
            playing = False
            print("You Win!\n")
        elif player.castle <= 0:
            playing = False
            print("You Lose!")
        else:
            os.system('clear')

if __name__ == '__main__':
    game_loop()
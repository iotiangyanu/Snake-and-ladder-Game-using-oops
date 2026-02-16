from players import Players
from board import Board

class Player: 

    @staticmethod
    def start_the_game():

        num_of_player=0
        while num_of_player<1:
            num_of_player=input("Enter number of Player want to play: ")
            num_of_player = ' '.join(num_of_player.split())
            if num_of_player.isdigit() is False or int(num_of_player) < 1:
                print("Enter valid player count")
                num_of_player=0
                
            else:
                num_of_player=int(num_of_player)
        list_of_player_name=[]

        player_score={}
        player_number=1

        while player_number<=num_of_player:
            player_name=input(f"Enter the name of player {player_number} without any space: ")
            player_name = ' '.join(player_name.split())

            if player_name in player_score or player_name.isspace() or player_name=="" or not player_name.isalpha():
                print("Please enter Unique Name and valid Name")

            else:
                list_of_player_name.append(player_name)
                player_score[player_name]=0
                player_number+=1
            
        board=Board(player_score)

        while True:
            for i in list_of_player_name:
                print("Hi ,",i)
                input("Press ENTER to play your round")
                print("Enter is pressed.")
                l=len(list_of_player_name)

                score=player_score[i]
                player_score[i]=board.start_game(i,l,score)

                score_of_last_played_player=player_score[i]

                if score_of_last_played_player == 100:
                    print(f"Hip Hip Hurray! {i} Won the Game 🎉")
                    return
            
while True:
    temp=input("You want to play new Game\n'For YES write Y or For NO write N'")
    temp = ' '.join(temp.split())
    if temp=="N" or temp=="n":
        print("Game Exited.")
        break
    elif temp=="y" or temp=="Y":
        Player.start_the_game()
    else:
        print("You Entered invalid command plase enter valid command ")

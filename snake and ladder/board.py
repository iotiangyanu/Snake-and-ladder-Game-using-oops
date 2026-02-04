import random

class Board:
    def __init__(self,player_score):
        self.player_score=player_score

    def start_game(self,player,l,score):
        dice=random.randint(1,6)
        if score==0 and dice!=6:
            print(f"Hey! You got the {dice}")
            return self.unable_to_unlock(l,player)
        
        elif score==0 and dice==6:
            print(f"Hey! You got the {dice}")
            print("You are Unlocked")
            current=score + 1
            return self.check_snake_ladder(current)

        else:
            print(f"Hey! You got the {dice}")
            current=score +  dice

            if current>100:
                if l>1:
                    print("Hey, You got Large Value")
                    print(f"{player} Wait for next Round")
                    print(f"You are on {self.player_score[player]}")
                    return self.player_score[player]
                else:
                    print(f"You are on {self.player_score[player]}")
                    print("Roll the Dice Again ")
                    return self.player_score[player]
                
            return self.check_snake_ladder(current)
    
    def unable_to_unlock(self, l, player):
        if l > 1:
            print("Hey, You got smaller Value")
            print(f"You are on {self.player_score[player]}")
            print(f"{player} Wait for next Round")
        else:
            print(f"You are on {self.player_score[player]}")
            print("Roll the Dice Again ")
        return self.player_score[player]
        

    def check_snake_ladder(self,squ):
        # List of all square with snake
        snake={14,19,25,38,51,68,74,93,97}
        # List of all square with Ladder
        ladder={5,20,27,36,43,55,67,83}

        if squ in snake:
            print(f"Now you are on {squ}")
            return self.check_snake(squ)

        elif squ in ladder:
            print(f"Now you are on {squ}")
            return self.check_ladder(squ)
        else:
            return self.move_forward(squ)

    def check_snake(self, squ):
        snake={
            14:7,
            19:3,
            25:18,
            38:19,
            51:9,
            68:37,
            74:58,
            93:50,
            97:1
        }
        current=snake[squ]
        print("Oops! Snake 🐍 bit you \n Now you are on ",current)
        return current
    def check_ladder(self, squ):
        ladder={
            5:26,
            20:21,
            27:45,
            36:63,
            43:96,
            55:78,
            67:92,
            83:95
        }
        current=ladder[squ]
        print("Hurray! you got a ladder 🪜\n Now you are on ",current)
        
        return ladder[squ]

    def move_forward(self, squ):
        print("Now you are on ",squ)
        return squ
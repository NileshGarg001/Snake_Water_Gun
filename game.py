def game_win(comp, you):
    if comp == "s":
        if you == "s":
            return "Tie"
        elif you == "w":
            return "Computer wins"
        else:
            return "You Win"
    if comp == "w":
        if you == "w":
            return "Tie"
        elif you == "g":
            return "Computer wins"
        else:
            return "You Win"
    else:
        if you == "g":
            return "Tie"
        elif you == "s":
            return "Computer wins"
        else:
            return "You Win"
        
import random
while True:
    print("Enter s for Snake, w for Water, g for Gun and e to Exit : ")
    play = ["s","w","g"]
    user = input("Your Choice : ") 
    if user not in play:
        if user == "e":
            print("Game over")
            break
        else:
            print("Kindly enter correct choice")
            continue
    comp = random.choice(play)
    print(f"Your Choice {user}")
    print(f"Computer chose {comp}")
    print(game_win(user, comp))
import random, time
from secret import FLAG

banner = """                                             
8 888888888o.   8 888888888o     d888888o.   
8 8888    `88.  8 8888    `88. .`8888:' `88. 
8 8888     `88  8 8888     `88 8.`8888.   Y8 
8 8888     ,88  8 8888     ,88 `8.`8888.     
8 8888.   ,88'  8 8888.   ,88'  `8.`8888.    
8 888888888P'   8 888888888P'    `8.`8888.   
8 8888`8b       8 8888            `8.`8888.  
8 8888 `8b.     8 8888        8b   `8.`8888. 
8 8888   `8b.   8 8888        `8b.  ;8.`8888 
8 8888     `88. 8 8888         `Y8888P ,88P' 

    Rocket       Paper            Scissors
"""

random.seed(time.time())
win = 0

print(banner)

for i in range(1000):
    if win == 100:
        print(FLAG)
    else:
        random_object = random.getrandbits(32)
        moves = ["rock", "paper", "scissors"]
        server_move = moves[random_object % 3]

        user_move = input("Enter rock, paper, or scissors: ").strip().lower()
        if user_move not in moves:
            print("Invalid choice! Enter rock, paper, or scissors.")

        else:
            result_message = f"\nThe server chose {server_move} as the random value was {random_object}."

            if user_move == server_move:
                win = 0 
                print(f"It's a tie!{result_message}")
            elif (user_move == "rock" and server_move == "scissors") or (user_move == "paper" and server_move == "rock") or (user_move == "scissors" and server_move == "paper"):
                win += 1
                print(f"You win!{result_message}\n You have {win} wins")
            else:
                win = 0
                print(f"You lose!{result_message}")
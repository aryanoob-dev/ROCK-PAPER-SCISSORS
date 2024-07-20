import random

def get_kid_choice():
    return input("Choose rock, paper, or scissors: ").lower()

def get_robot_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def find_winner(kid, robot):
    if kid == robot:
        return "It's a tie!"
    elif (kid == "rock" and robot == "scissors") or \
         (kid == "scissors" and robot == "paper") or \
         (kid == "paper" and robot == "rock"):
        return "You win!"
    else:
        return "You lose!"

def show_result(kid, robot, outcome):
    print(f"You chose: {kid}")
    print(f"Robot chose: {robot}")
    print(outcome)

def play_fun_game():
    kid_score = 0
    robot_score = 0
    
    while True:
        kid_choice = get_kid_choice()
        robot_choice = get_robot_choice()
        outcome = find_winner(kid_choice, robot_choice)
        
        show_result(kid_choice, robot_choice, outcome)
        
        if outcome == "You win!":
            kid_score += 1
        elif outcome == "You lose!":
            robot_score += 1
        
        print(f"Your score: {kid_score}")
        print(f"Robot's score: {robot_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

play_fun_game()

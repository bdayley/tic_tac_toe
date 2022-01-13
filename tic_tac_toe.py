"""
Your program must also meet the following requirements.
    The program must have a comment with assignment and author names.
    The program must have at least one if/then block.
    The program must have at least one while loop.
    The program must have more than one function.
    The program must have a function called main.
"""

# W02 Prove: Developer - Solo Code Submission
# Tic Tac Toe
# Author: Brianna Dayley

# TODO:
# check if square has already been taken
# if input is invalid, don't add to counter

def main():
    print("Tic Tac Toe")
    print()
    play_game()


def display_grid(the_list):
    for item in the_list:
        print(item, end = "")
    print()

def ask_for_input(player):
    valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # input returns a string
    answer = input(f"{player}'s turn to choose a square (1-9): ")   # need to check if answer is valid
    if answer in valid_numbers:
        return answer
    else:
        print("invalid option, try again")

def play_game():
    game_complete = False
    counter = 1 #to check whose turn it is (X or O)
    
    the_list = ["1", "|", "2", "|", "3", "\n-+-+-\n", "4", "|", "5", "|", "6", "\n-+-+-\n", "7", "|", "8", "|", "9"]
    
    display_grid(the_list)
    print()
    
    while game_complete == False:
        if counter % 2 != 0:
            player = "X"
        else:
            player = "O"
        answer = ask_for_input(player)
        if answer == "1":
            the_list[0] = player
        elif answer == "2":
            the_list[2] = player
        elif answer == "3":
            the_list[4] = player
        elif answer == "4":
            the_list[6] = player
        elif answer == "5":
            the_list[8] = player
        elif answer == "6":
            the_list[10] = player
        elif answer == "7":
            the_list[12] = player
        elif answer == "8":
            the_list[14] = player
        elif answer == "9":
            the_list[16] = player
        counter += 1

        game_complete = check_win(the_list)
        if game_complete == True:
            print()
            print("Good game!")

        if counter == 10: # use this for now so it's not an infinite loop
            game_complete = True

        print()
        display_grid(the_list)
        print()
    
    return the_list

def check_win(the_list):
    # ways to win - there's gotta be a more efficient way to do this!?

    # check if "X" wins
    # rows
    if the_list[0] == "X" and the_list[2] == "X" and the_list[4] == "X":
        return True
    if the_list[6] == "X" and the_list[8] == "X" and the_list[10] == "X":
        return True
    if the_list[12] == "X" and the_list[14] == "X" and the_list[16] == "X":
        return True
    
    # columns
    if the_list[0] == "X" and the_list[6] == "X" and the_list[12] == "X":
        return True
    if the_list[2] == "X" and the_list[8] == "X" and the_list[14] == "X":
        return True
    if the_list[4] == "X" and the_list[10] == "X" and the_list[16] == "X":
        return True

    # diagonal
    if the_list[0] == "X" and the_list[8] == "X" and the_list[16] == "X":
        return True
    if the_list[12] == "X" and the_list[8] == "X" and the_list[4] == "X":
        return True


    # check if "O" wins
    # rows
    if the_list[0] == "O" and the_list[2] == "O" and the_list[4] == "O":
        return True
    if the_list[6] == "O" and the_list[8] == "O" and the_list[10] == "O":
        return True
    if the_list[12] == "O" and the_list[14] == "O" and the_list[16] == "O":
        return True
    
    # columns
    if the_list[0] == "O" and the_list[6] == "O" and the_list[12] == "O":
        return True
    if the_list[2] == "O" and the_list[8] == "O" and the_list[14] == "O":
        return True
    if the_list[4] == "O" and the_list[10] == "O" and the_list[16] == "O":
        return True

    # diagonal
    if the_list[0] == "O" and the_list[8] == "O" and the_list[16] == "O":
        return True
    if the_list[12] == "O" and the_list[8] == "O" and the_list[4] == "O":
        return True
    
    return False
    
    
    


if __name__ == "__main__":
    main()
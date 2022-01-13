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

def main():
    print("Tic Tac Toe")
    print()
    the_list = ask_for_input()
    #display_grid(the_list)

def display_grid(the_list):
    for item in the_list:
        print(item, end = "")
    print()

def ask_for_input(): # this function does too many things, need to seperate out some things
    game_complete = False
    counter = 1 #to check whose turn it is (X or O)
    
    the_list = ["1", "|", "2", "|", "3", "\n-+-+-\n", "4", "|", "5", "|", "6", "\n-+-+-\n", "7", "|", "8", "|", "9"]
    
    display_grid(the_list)
    
    while game_complete == False:
        if counter % 2 != 0:
            player = "X"
        else:
            player = "O"
        answer = input(f"{player}'s turn to choose a square (1-9): ")   # need to check if answer is valid     
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
        else:
            print("invalid option") # check a different way cuz this doesn't stop the counter from adding one
        counter += 1
        if counter == 10: # use this for now so it's not an infinite loop
            game_complete = True
        #check if game complete
        print()
        display_grid(the_list)
        print()
    
    return the_list

def play_game(answer):
    


if __name__ == "__main__":
    main()
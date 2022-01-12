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
    game_complete = False
    the_list = []
    #while game_complete == False:
        # ask_for_input()
        # need a way to check if game complete- do in ask_for_input?
    #    pass
    display_grid(the_list)

def display_grid(the_list):
    for item in the_list:
        print(item, end = "")
    print()

def ask_for_input():
    # need to alternate turns (x and o)
    # need to check if answer is valid
    
    the_list = ["1", "|", "2", "|", "3", "\n-+-+-\n", "4"]
    answer = input("x's turn to choose a square(1-9): ")
    # check for game complete here?
    # change list here?
    return the_list


if __name__ == "__main__":
    main()
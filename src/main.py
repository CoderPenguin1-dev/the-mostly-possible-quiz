#!/bin/python
import turtle  
from questions import *
import display
from globals import *

turtle.setup(800, 800)
wn = turtle.Screen()
quit_invoked : bool = False
current_question : int = 0

def main() -> None:
    # Initalize input.
    wn.onkeypress(answer1_selected, "a") # Option 1.
    wn.onkeypress(answer2_selected, "b") # Option 2.
    wn.onkeypress(answer3_selected, "c") # Option 3.
    wn.onkeypress(answer4_selected, "d") # Option 4.
    wn.onkeypress(quit_game, "q") # Quit.
    wn.listen()

    while (not quit_invoked):
       display.clear()
       draw_game()
       turtle.update()

def draw_game() -> None:
    global game_state
    match game_state:
        case GameStates.MAIN_MENU:
            display.main_menu()
        case GameStates.QUESTIONS:
            display.question(current_question)
            display.question_number(current_question)
        case GameStates.GAME_OVER_MSG:
            display.game_over()
        case GameStates.GAME_OVER:
            display.wipe("red")
            game_state = GameStates.GAME_OVER_MSG
        case GameStates.CORRECT_ANSWER:
            display.wipe("green")
            game_state = GameStates.QUESTIONS
        case GameStates.YOURE_WINNER:
            display.wipe("yellow")
            game_state = GameStates.GAME_WIN_MSG
        case GameStates.GAME_WIN_MSG:
            display.game_won()

    display.scroll_banner()

def check_answer(answer_index : int) -> None:
    global current_question
    global game_state
    if (game_state == GameStates.QUESTIONS):
        if (QUESTIONS[current_question].answer == answer_index):
            current_question += 1
            game_state = GameStates.CORRECT_ANSWER
        else: game_state = GameStates.GAME_OVER
        
        if (current_question == QUESTION_AMOUNT):
            game_state = GameStates.YOURE_WINNER
    else:
        current_question = 0
        game_state = GameStates.QUESTIONS

def answer1_selected() -> None:
    check_answer(0)

def answer2_selected() -> None:
    check_answer(1)

def answer3_selected() -> None:
    check_answer(2)

def answer4_selected() -> None:
    check_answer(3)

def quit_game() -> None:
    global quit_invoked
    quit_invoked = True

if __name__ == "__main__":
    main()

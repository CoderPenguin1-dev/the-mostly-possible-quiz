import turtle  
from questions import *
import display
from globals import *

turtle.setup(800, 800)
wn = turtle.Screen()
quit_invoked : bool = False

current_question : int = 0

def draw_game():
    if (game_running):
        display.question(current_question)
        display.question_number(current_question)
        display.wipe_shown = False
    else: 
        display.game_over()
    display.scroll_banner()

def check_answer(answer_index : int):
   global current_question
   global game_running
   if (game_running):
      if (questions[current_question].answer == answer_index):
         current_question += 1
      else: game_running = False
      
      if (current_question == question_amount):
         game_running = False
   else:
      current_question = 0
      game_running = True

def answer1_selected():
   check_answer(0)

def answer2_selected():
   check_answer(1)

def answer3_selected():
   check_answer(2)

def answer4_selected():
   check_answer(3)

def quit_game():
   global quit_invoked
   quit_invoked = True

def main():
    wn.onkeypress(answer1_selected, "a")
    wn.onkeypress(answer2_selected, "b")
    wn.onkeypress(answer3_selected, "c")
    wn.onkeypress(answer4_selected, "d")
    wn.onkeypress(quit_game, "q")
    wn.listen()

    while (not quit_invoked):
       display.clear()
       draw_game()
       turtle.update()

if __name__ == "__main__":
    main()

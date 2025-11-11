import turtle  
from questions import *
import display
from globals import *

turtle.setup(800, 800)
wn = turtle.Screen()

def draw_game():
	display.clear()
	if (game_running):
		display.question(current_question)
	else: 
		display.game_over()

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
   draw_game()

def answer1_selected():
   check_answer(0)

def answer2_selected():
   check_answer(1)

def answer3_selected():
   check_answer(2)

def answer4_selected():
   check_answer(3)

def main():
	draw_game()
	wn.onkeypress(answer1_selected, "a")
	wn.onkeypress(answer2_selected, "b")
	wn.onkeypress(answer3_selected, "c")
	wn.onkeypress(answer4_selected, "d")
	wn.listen()
	wn.mainloop()

if __name__ == "__main__":
    main()

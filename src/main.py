import turtle  
from question import Question
from questions import *
import fonts
import constants

questions : list[Question] = [question1, question2, question3, question4, question5, question6]
question_amount : int = len(questions)
turtle.setup(800, 800)
wn = turtle.Screen()
game_over : bool = False
current_question : int = 0

# Turtles
question_writer = turtle.Turtle()
question_writer.hideturtle()
question_writer.penup()
question_writer.goto(-100,100)

answer1_writer = turtle.Turtle()
answer1_writer.hideturtle()
answer1_writer.penup()
answer1_writer.goto(-90,50)

answer2_writer = turtle.Turtle()
answer2_writer.hideturtle()
answer2_writer.penup()
answer2_writer.goto(-90,0)

answer3_writer = turtle.Turtle()
answer3_writer.hideturtle()
answer3_writer.penup()
answer3_writer.goto(-90,-50)

answer4_writer = turtle.Turtle()
answer4_writer.hideturtle()
answer4_writer.penup()
answer4_writer.goto(-90,-100)

gameover_writer = turtle.Turtle()
gameover_writer.penup()
gameover_writer.hideturtle()
gameover_writer.pencolor("red")
gameover_writer.goto(-180, 0)

wipe_drawer = turtle.Turtle()
wipe_drawer.hideturtle()
wipe_drawer.speed(0)
wipe_drawer.pensize(constants.WIPE_SPEED)
wipe_drawer.pencolor("red")


def display_question(question_number : int):
  question_writer.write(questions[question_number].question, font=fonts.question)
  answer1_writer.write("A) "+ questions[question_number].answers[0],font=fonts.answers)
  answer2_writer.write("B) "+ questions[question_number].answers[1],font=fonts.answers)
  answer3_writer.write("C) "+ questions[question_number].answers[2],font=fonts.answers)
  answer4_writer.write("D) "+ questions[question_number].answers[3],font=fonts.answers)

def display_game_over():
   display_wipe(constants.GAMEOVER_WIPE_COLOR)
   gameover_writer.write("Game Over!", font=fonts.gameover)

def display_wipe(color : str):
  wipe_drawer.pencolor(color)
  window_width = turtle.window_width()
  # -350 to compensate for the window being larger than actually being shown.
  window_height = turtle.window_height() - 350

  # Goto inital position.
  wipe_drawer.penup()
  wipe_drawer.goto(-window_width, window_height)
  
  y = window_height
  while y >= -window_height + constants.WIPE_CLEAR_DELAY: # The +10 is there to add a delay from when the wipe is cleared.
     wipe_drawer.pendown()
     wipe_drawer.goto(-window_width, y)
     y -= constants.WIPE_SPEED
     wipe_drawer.penup()
     wipe_drawer.goto(window_width, y)
     
  wipe_drawer.clear()

def draw_game():
	question_writer.clear()
	answer1_writer.clear()
	answer2_writer.clear()
	answer3_writer.clear()
	answer4_writer.clear()

	if (game_over):
		display_game_over()
	else: display_question(current_question)

def check_answer(answer_index : int):
	global current_question
	global game_over
	if (questions[current_question].answer == answer_index):
		current_question += 1
	else: game_over = True
    
	if (current_question > question_amount):
		game_over = True
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
	game_over : bool = False
	current_question : int = 0

	draw_game()
	wn.onkeypress(answer1_selected, "a")
	wn.onkeypress(answer2_selected, "b")
	wn.onkeypress(answer3_selected, "c")
	wn.onkeypress(answer4_selected, "d")
	wn.listen()
	wn.mainloop()

if __name__ == "__main__":
    main()

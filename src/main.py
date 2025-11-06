import turtle  
from question import Question
from questions import *
import fonts
import constants
questions : list[Question] = [question1, question2]
question_amount : int = len(questions)
turtle.setup(800, 800)
wn = turtle.Screen()

# Turtles
question_writer = turtle.Turtle()
answer1_writer = turtle.Turtle()
answer2_writer = turtle.Turtle()
answer3_writer = turtle.Turtle()
answer4_writer = turtle.Turtle()

gameover_writer = turtle.Turtle()
gameover_writer.penup()
gameover_writer.hideturtle()
gameover_writer.pencolor("red")
gameover_writer.goto(-180, 0)

wipe_drawer = turtle.Turtle()
wipe_drawer.speed(0)
wipe_drawer.pensize(constants.WIPE_SPEED)
wipe_drawer.pencolor("red")


def display_question(question_number : int):
  pass

def display_game_over():
   display_wipe()
   gameover_writer.write("Game Over!", font=fonts.gameover)

def display_wipe():
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

def main():
  wn.mainloop()

if __name__ == "__main__":
    main()

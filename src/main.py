import turtle  
from question import Question
from questions import *
import fonts
questions : list[Question] = [question1, question2]
question_amount : int = len(questions)
turtle.setup(800, 800)
wn = turtle.Screen()

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

wipe_drawer = turtle.Turtle()
wipe_drawer.speed(0)
wipe_drawer.pensize(30)
wipe_drawer.pencolor("red")


def display_question(question_number : int):
  question_writer.write(questions[question_number].question, font=fonts.question)
  answer1_writer.write("A) "+ questions[question_number].answers[0],font=fonts.answers)
  answer2_writer.write("B) "+ questions[question_number].answers[1],font=fonts.answers)
  answer3_writer.write("C) "+ questions[question_number].answers[2],font=fonts.answers)
  answer3_writer.write("D) "+ questions[question_number].answers[3],font=fonts.answers)

def display_game_over():
   pass

def display_wipe():
  window_width = turtle.window_width()
  # -350 to compensate for the window being larger than actually being shown.
  window_height = turtle.window_height() - 350

  # Goto inital position.
  wipe_drawer.penup()
  wipe_drawer.goto(-window_width, window_height)
  
  y = window_height
  while y >= -window_height + 10: # The +10 is there to add a delay from when the wipe is cleared.
     wipe_drawer.pendown()
     wipe_drawer.goto(-window_width, y)
     y -= 30
     wipe_drawer.penup()
     wipe_drawer.goto(window_width, y)
     
  wipe_drawer.clear()

def main():
  wn.mainloop()

if __name__ == "__main__":
    main()

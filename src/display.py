import turtle
import constants
from globals import *
import fonts

turtle.tracer(0)
turtle.update()

# Turtles

question_writer = turtle.Turtle()
question_writer.hideturtle()
question_writer.penup()
question_writer.goto(constants.QUESTION_X_POS, constants.QUESTION_Y_POS)

answer1_writer = turtle.Turtle()
answer1_writer.hideturtle()
answer1_writer.penup()
answer1_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET)
answer1_writer.pencolor("red")

answer2_writer = turtle.Turtle()
answer2_writer.hideturtle()
answer2_writer.penup()
answer2_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 2)
answer2_writer.pencolor("green")

answer3_writer = turtle.Turtle()
answer3_writer.hideturtle()
answer3_writer.penup()
answer3_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 3)
answer3_writer.pencolor("blue")

answer4_writer = turtle.Turtle()
answer4_writer.hideturtle()
answer4_writer.penup()
answer4_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 4)
answer4_writer.pencolor("orange")

game_over_writer = turtle.Turtle()
game_over_writer.penup()
game_over_writer.hideturtle()
game_over_writer.pencolor("red")
game_over_writer.goto(-260, -20)

wipe_drawer = turtle.Turtle()
wipe_drawer.hideturtle()
wipe_drawer.speed(0)
wipe_drawer.pensize(constants.WIPE_SPEED)
wipe_drawer.pencolor("red")
#def quizer_drawer():

quizer_drawer = turtle.Turtle()
quizer_drawer.penup()
quizer_drawer.goto(-390,330)
quizer_drawer.write("The Mostly Possible Quiz")
for i in range(6):
  quizer_drawer.forward(150)
  quizer_drawer.write("The Mostly Possible Quiz")


turtle.tracer(1)

def question(question_number : int):
  question_writer.write(questions[question_number].question, font=fonts.question)
  answer1_writer.write("A) "+ questions[question_number].answers[0],font=fonts.answers)
  answer2_writer.write("B) "+ questions[question_number].answers[1],font=fonts.answers)
  answer3_writer.write("C) "+ questions[question_number].answers[2],font=fonts.answers)
  answer4_writer.write("D) "+ questions[question_number].answers[3],font=fonts.answers)

def game_over():
   wipe(constants.GAMEOVER_WIPE_COLOR)
   game_over_writer.write("     Game Over!\nPress A to restart.", font=fonts.gameover)

def wipe(color : str):
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

def clear():
    question_writer.clear()
    game_over_writer.clear()
    answer1_writer.clear()
    answer2_writer.clear()
    answer3_writer.clear()
    answer4_writer.clear()
import turtle
import constants
from globals import *
import fonts
from time import sleep

turtle.tracer(0)

'''
    Turtles
'''
# Question Text
question_writer = turtle.Turtle()
question_writer.hideturtle()
question_writer.penup()
question_writer.goto(constants.QUESTION_X_POS, constants.QUESTION_Y_POS)

# Answer Text
answer1_writer = turtle.Turtle()
answer1_writer.hideturtle()
answer1_writer.penup()
answer1_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET)

answer2_writer = turtle.Turtle()
answer2_writer.hideturtle()
answer2_writer.penup()
answer2_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 2)

answer3_writer = turtle.Turtle()
answer3_writer.hideturtle()
answer3_writer.penup()
answer3_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 3)

answer4_writer = turtle.Turtle()
answer4_writer.hideturtle()
answer4_writer.penup()
answer4_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 4)

# Game Over Text
game_over_writer = turtle.Turtle()
game_over_writer.penup()
game_over_writer.hideturtle()
game_over_writer.pencolor("red")
game_over_writer.goto(-280, -20)

# Wipe Screen
wipe_drawer = turtle.Turtle()
wipe_drawer.hideturtle()
wipe_drawer.pensize(constants.WIPE_SPEED)
wipe_drawer.pencolor("red")

# Scrolling Banner
banner_position : float = -constants.BANNER_X_BOUND
banner_writer = turtle.Turtle()
banner_writer.hideturtle()
banner_writer.penup()
banner_writer.pencolor("green")
banner_writer.goto(banner_position, constants.BANNER_Y_POS)

# Question Number
question_number_writer = turtle.Turtle()
question_number_writer.hideturtle()
question_number_writer.penup()
question_number_writer.goto(250, -350)

# Main Menu
main_menu_writer = turtle.Turtle()
main_menu_writer.hideturtle()
main_menu_writer.penup()
main_menu_writer.goto(-240, -50)

def main_menu():
    main_menu_writer.write("Press A to Start\n           or\n     Q to Quit!", font=fonts.gameover)

def question(question_number : int):
  question_writer.write(questions[question_number].question, font=fonts.question)
  answer1_writer.write("A) "+ questions[question_number].answers[0], font=fonts.answers)
  answer2_writer.write("B) "+ questions[question_number].answers[1], font=fonts.answers)
  answer3_writer.write("C) "+ questions[question_number].answers[2], font=fonts.answers)
  answer4_writer.write("D) "+ questions[question_number].answers[3], font=fonts.answers)

def question_number(current_question : int):
    question_number_writer.write(f"#{current_question:02d}", font=fonts.question_number)

def game_over():
   game_over_writer.write("     Game Over!\n\nPress A to restart.\n  Press Q to quit.", font=fonts.gameover)

def scroll_banner():
    global banner_position

    # Move the banner right. Check to see if it needs to be looped over.
    banner_position += 10
    if (banner_position == constants.BANNER_X_BOUND):
        banner_position = -constants.BANNER_X_BOUND

    banner_writer.goto(banner_position, constants.BANNER_Y_POS)
    banner_writer.write("The Mostly Possible Quiz", font=fonts.banner)
    sleep(0.05)

def wipe(color : str):
    # Hide the banner. Othrwise it'll be obvious it stopped moving.
    banner_writer.clear()

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
        sleep(0.03)
        turtle.update()
        
    wipe_drawer.clear()


def clear():
    main_menu_writer.clear()
    question_writer.clear()
    question_number_writer.clear()
    game_over_writer.clear()
    answer1_writer.clear()
    answer2_writer.clear()
    answer3_writer.clear()
    answer4_writer.clear()
    banner_writer.clear()
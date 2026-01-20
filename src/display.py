import turtle
import constants
from globals import *
import fonts
from time import sleep

turtle.tracer(0)

#
#   Turtle Definitions
#

#region Question Text
question_writer = turtle.Turtle()
question_writer.hideturtle()
question_writer.penup()
question_writer.goto(constants.QUESTION_X_POS, constants.QUESTION_Y_POS)
#endregion

#region Answer 1 Text
answer1_writer = turtle.Turtle()
answer1_writer.hideturtle()
answer1_writer.penup()
answer1_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET)
answer1_writer.pencolor("red")
#endregion

#region Answer 2 Text
answer2_writer = turtle.Turtle()
answer2_writer.hideturtle()
answer2_writer.penup()
answer2_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 2)
answer2_writer.pencolor("blue")
#endregion

#region Answer 3 Text
answer3_writer = turtle.Turtle()
answer3_writer.hideturtle()
answer3_writer.penup()
answer3_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 3)
answer3_writer.pencolor("green")
#endregion

#region Answer 4 Text
answer4_writer = turtle.Turtle()
answer4_writer.hideturtle()
answer4_writer.penup()
answer4_writer.goto(constants.QUESTION_X_POS + 20, constants.QUESTION_Y_POS - constants.ANSWER_Y_OFFSET * 4)
answer4_writer.pencolor("orange")
#endregion

#region Game Over Text
game_over_writer = turtle.Turtle()
game_over_writer.penup()
game_over_writer.hideturtle()
game_over_writer.pencolor("red")
game_over_writer.goto(-360, -80)
#endregion

#region Wipe Screen
wipe_drawer = turtle.Turtle()
wipe_drawer.hideturtle()
wipe_drawer.pensize(constants.WIPE_SPEED)
wipe_drawer.pencolor("red")
#endregion

#region Scrolling Banner
banner_position : float = -constants.BANNER_X_BOUND
banner_writer = turtle.Turtle()
banner_writer.hideturtle()
banner_writer.penup()
banner_writer.pencolor("green")
banner_writer.goto(banner_position, constants.BANNER_Y_POS)
#endregion

#region Question Number
question_number_writer = turtle.Turtle()
question_number_writer.hideturtle()
question_number_writer.penup()
question_number_writer.goto(250, -350)
#endregion

#region Main Menu
main_menu_writer = turtle.Turtle()
main_menu_writer.hideturtle()
main_menu_writer.penup()
main_menu_writer.goto(-300, -50)
#endregion


def main_menu() -> None:
    main_menu_writer.write("Press A to Start\n           or\n     Q to Quit!", font=fonts.gameover)

def question(question_number : int) -> None:
    question_writer.write(QUESTIONS[question_number].question, font=fonts.question)
    answer1_writer.write("A) "+ QUESTIONS[question_number].answers[0], font=fonts.answers)
    answer2_writer.write("B) "+ QUESTIONS[question_number].answers[1], font=fonts.answers)
    answer3_writer.write("C) "+ QUESTIONS[question_number].answers[2], font=fonts.answers)
    answer4_writer.write("D) "+ QUESTIONS[question_number].answers[3], font=fonts.answers)

def question_number(current_question : int) -> None:
    question_number_writer.write(f"#{current_question + 1:02d}", font=fonts.question_number)

def game_over() -> None:
    game_over_writer.write("     Game Over!\n\nPress A to restart.\n  Press Q to quit.", font=fonts.gameover)

def game_won() -> None:
    game_over_writer.write("     You Won!\n\nPress A to restart.\n  Press Q to quit.", font=fonts.gameover)

def scroll_banner() -> None:
    global banner_position

    # Move the banner right. Check to see if it needs to be looped over.
    banner_position += 10
    if (banner_position == constants.BANNER_X_BOUND):
        banner_position = -constants.BANNER_X_BOUND

    banner_writer.goto(banner_position, constants.BANNER_Y_POS)
    banner_writer.write("The Mostly Possible Quiz", font=fonts.banner)
    sleep(0.05)

def wipe(color : str) -> None:
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

def clear() -> None:
    main_menu_writer.clear()
    question_writer.clear()
    question_number_writer.clear()
    game_over_writer.clear()
    answer1_writer.clear()
    answer2_writer.clear()
    answer3_writer.clear()
    answer4_writer.clear()
    banner_writer.clear()
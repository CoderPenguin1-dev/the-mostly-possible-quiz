import turtle  
from question import Question
from questions import *
import fonts
questions : list[Question] = [question1, question2]
question_amount : int = len(questions)

# Turtles
question_writer = turtle.Turtle()
answer1_writer = turtle.Turtle()
answer2_writer = turtle.Turtle()
answer3_writer = turtle.Turtle()
answer4_writer = turtle.Turtle()
gameover_writer = turtle.Turtle()

def display_question(question_number : int):
  pass

def display_game_over():
   pass

def main():
  current_question : int = 0
  print(question2.question)
  for answer in question2.answers:
     print(answer)

if __name__ == "__main__":
    main()
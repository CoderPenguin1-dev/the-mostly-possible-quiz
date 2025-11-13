from enum import Enum
class GameStates(Enum):
    MAIN_MENU = 0
    GAME_OVER_MSG = 1
    GAME_OVER = 2
    QUESTIONS = 3
    CORRECT_ANSWER = 4
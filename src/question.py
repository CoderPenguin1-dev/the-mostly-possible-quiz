from question_answer import Answer
class Question:
    question : str
    answers : list[str]
    answer : Answer

    def __init__(self, question : str, answers : list[str], answer : int) -> None:
        self.question = question
        self.answers = answers
        self.answer = answer

        # Value checks
        if (self.answer.value > 3 or self.answer.value < 0):
            raise ValueError("Question answer index is out of range.")
        
        if (len(self.answers) != 4):
            raise ValueError("Too many or not enough answers.")

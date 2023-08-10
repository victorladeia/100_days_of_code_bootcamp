class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        question = self.question_list[self.question_number]
        input(f"Q.{self.question_number+1}: {question.text} (True/False): ")

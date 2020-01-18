class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompt = [
    'Which is the best computer language? \n(a) C#.\n(b) JavaScript.\n(c) Python.\n',
    'Which is the best course at Lambton College? \n(a) CSAT.\n(b) CISC.\n(c) EPMS.\n',
    'Who is the best professor at Lambton College? \n(a) Hessam Akbari.\n(b) Option A.\n(c) Option B.\n',
]


questions = [
    Question(question_prompt[0], 'c'),
    Question(question_prompt[1], 'a'),
    Question(question_prompt[2], 'a'),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('Congratulations! You got ' + str(score) + '/' + str(len(questions)) + ' correct.')


run_test(questions)

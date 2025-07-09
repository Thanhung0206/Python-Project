class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n ",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def tinh_diem(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt) #Truy cập trong questions rồi đến prompt trong Question
        if answer == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

tinh_diem(questions)


#B1: Tạo Clas Question để lưu trữ 2 tham số: Câu hỏi và đáp án
#B2: Tạo question_prompts để lưu bộ câu hỏi 
#B3: Tạo questions để gán bộ câu hỏi và bộ đáp án tương ứng với 2 tham số trong Question
#B4: Tạo hàm def để thực hiện tính toán
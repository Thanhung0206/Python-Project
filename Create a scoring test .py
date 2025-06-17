class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
#Tạo câu hỏi --> để học sinh trả lời
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n ",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n"
]
#Tạo bộ câu hỏi kèm đáp án
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

#Tính điểm dựa trên câu trả lời
def tinh_diem(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt) #Truy cập trong questions rồi đến prompt trong Question
        if answer == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

tinh_diem(questions)

#Nên dùng class nếu không sẽ phải dùng for i in range len... và phải input(...[i])

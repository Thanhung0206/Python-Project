import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])#choice để random trong 1 list/tuple/strings

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):# được dùng hàm is_win vì được gán biến = hàm trong hàm và không cần ==True
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

#B1: Tạo hàm phân định kết quả play()
#B2: Tạo hàm logic thắng thua ( quy luật trò chơi)
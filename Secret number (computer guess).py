import random
def computer_guess(x): # Để máy đoán secret của mình
    low = 1 # B1: Tạo low và high riêng (để còn code cách tư duy cho máy)
    high = x
    feedback = ''# do cần nhập h/l/c nên phải dùng "" để tránh lỗi chưa có biến feedback, nếu là int thì dùng = 0
    while feedback != 'c': #B2: Dùng while nếu đoán khác số mình chọn
        if low != high: # B3: Code cách tư duy cho máy (khi low != high mới có khoảng để đoán)
            guess = random.randint(low, high)
        else:
            guess = low  # nếu low=high thì guess = số ấy luôn
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower() # Máy hỏi để tư duy đoán tiếp
        if feedback == 'h': # Code cách tư duy cho máy khi đoán sai
            high = guess - 1 # Không phải +-1 sau mỗi lần máy đoán, máy sẽ đoán theo khoảng thấp/cao hơn khoảng random sai (bỏ số vừa chọn)
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')#B4: Print kết quả + lời khen 


computer_guess(10)
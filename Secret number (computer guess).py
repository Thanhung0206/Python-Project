import random
def computer_guess(x): # Để máy đoán secret của mình
    low = 1 
    high = x
    feedback = ''# do cần nhập h/l/c nên phải dùng "" để tránh lỗi chưa có biến feedback, nếu là int thì dùng = 0
    while feedback != 'c': 
        if low != high: # khi low != high mới có khoảng để đoán
            guess = random.randint(low, high)
        else:
            guess = low  # nếu low=high thì guess = số ấy luôn
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower() # Máy hỏi để tư duy đoán tiếp
        if feedback == 'h': # Code cách tư duy cho máy khi đoán sai
            high = guess - 1 # Không phải +-1 kết quả đoán, máy sẽ đoán trên hoặc dưới khoảng vd (1,guess-1)
        elif feedback == 'l':
            low = guess + 1 # máy sẽ đoán trên hoặc dưới khoảng vd (guess+1,10)

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(10)

#B1: Tạo low và high riêng (để còn code cách tư duy cho máy)
#B2: Dùng while nếu máy đoán khác số mình chọn
#B3: Code cách tư duy cho máy
#B4: Print kết quả + lời khen ngoài vòng while
import random

def guess(x): # Để mình đoán secret của máy
    random_number = random.randint(1, x)# Tạo random từ [1,x] do máy chọn
    guess = 0 # Tránh lỗi khi gọi biến guess ở while (không có tác dụng gì)
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) # Nhập dự đoán
        if guess < random_number: # gợi ý
            print('Sorry, guess again. Too low.')
        elif guess > random_number: # gợi ý
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

guess(10)

#B1: Dùng random.randint tạo khoảng random
#B2: Dùng vòng while nếu khác kết quả thì ttục nhập guess và đưa ra gợi ý trong while
#B3: In ra lời khen + kết quả ngoài vòng while vì đã đúng 
        
    
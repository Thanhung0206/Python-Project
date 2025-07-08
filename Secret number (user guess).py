import random

def guess(x): # Để mình đoán secret của máy
    random_number = random.randint(1, x)# B1: Tạo random từ [1,x] do máy chọn
    guess = 0 # Tránh lỗi khi gọi biến guess ở while (không có tác dụng gì)
    while guess != random_number:# B2: Dùng while, nếu đoán khác số computer chọn
        guess = int(input(f'Guess a number between 1 and {x}: ')) # Nhập dự đoán
        if guess < random_number: # B3: Đưa ra gợi ý
            print('Sorry, guess again. Too low.')
        elif guess > random_number: # gợi ý
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')# B4: in ra lời khen +kết quả

guess(10)

        
    
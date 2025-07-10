import random
from word_hangman import words
import string

#B1: Tạo 1 def để chọn random 1 từ hợp lệ 
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words) # Từ ko hợp lệ bắt nhập lại

    return word.upper()

#B2: Tạo def chính để thực thi
def hangman():
    word = get_valid_word(words) #Từ đã hợp lệ 
    word_letters = set(word)  # Set các chữ cái trong từ 
    alphabet = set(string.ascii_uppercase) # Set các chữ in hoa từ A-Z
    used_letters = set()  # Set các chữ cái đã nhập (lưu trữ)
    lives = 6 # 6 mạng

    while len(word_letters) > 0 and lives > 0:#Chừng nào người chơi chưa đoán hết và còn mạng thì ttục thực thi 
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))# Các chữ cái đã dùng
        word_list = [letter if letter in used_letters else '-' for letter in word] #VD: han-s-me (handsome)
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()#User nhập letter
        if user_letter in alphabet - used_letters:# TH1: Nếu nhập trong bảng chữ cái và không trong chữ cái đã nhập
            used_letters.add(user_letter)
            if user_letter in word_letters:# + Nếu nhập trùng chữ cái trong từ thì word_letter bỏ letter nhập đó
                word_letters.remove(user_letter)
                print('')

            else:# + Nếu nhập sai thì trừ 1 mạng
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:# TH2: Nếu nhập trong chữ cái đã nhập rồi
            print('\nYou have already used that letter. Guess another letter.')

        else:# TH3: Còn lại( nhập sai....)
            print('\nThat is not a valid letter.')

    if lives == 0:# hết mạng
        print('You died, sorry. The word was', word)
    else:# đoán trúng (khá hiếm tại có 6 mạng mà trung bình 1 từ gồm 5 chữ)
        print('YAY! You guessed the word', word, '!!')

hangman()
#list comprehension: [x for....if] hoặc [if...else...for]
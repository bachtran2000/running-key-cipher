import os
#  Định nghĩa không gian bảng mã ban đầu
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def isAlphabetic(string):
    leng_match = 0
    for i in string:
        if i in alphabet:
            leng_match += 1
        else:
            leng_match = leng_match
    if len(string) == leng_match:
        return True
    else:
        return False


def encode(plaintext, key):
    ciphertxt = ''
    ori_plain = plaintext
    ori_key = key
    # Xử lý chuỗi ban đầu
    key = key.replace(" ", "").lower().strip(" ")
    plaintext = plaintext.replace(" ", "").lower().strip(" ")
    if isAlphabetic(plaintext) and isAlphabetic(key):
        # Xét trường hợp cho phép nếu chiều dài chuỗi lớn hơn hoặc bằng chiều dài key
        if len(plaintext) >= len(key):
            # Tạo ra không gian khoá khoá hoàn chỉnh
            for i in plaintext:
                if len(key) < len(plaintext):
                    key = key + i
            for i in range(0, len(plaintext)):
                # lấy vị trí của phần tử thứ i
                pos = (alphabet.find(plaintext[i])+alphabet.find(key[i])) % 26
                # mã hoá ký tự vị trí thứ i
                ciphertxt = ciphertxt+alphabet[pos]
                print('Plain text in position',i+1,':',plaintext[i],'=',ciphertxt[i])
                print('key in position',i+1,':',key[i])

            print()
            print('Origin text:', ori_plain)
            print('Key:', ori_key)
            print('Encrypt:', ciphertxt.upper())
        else:
            print('Plain text must shorter than key!')
    else:
        print('A character out of space of key')


def decode(cipher, key):
    plaintext = ''
    ori_cipher = cipher
    ori_key = key
    cipher = cipher.replace(" ", "").lower().strip(" ")
    key = key.replace(" ", "").lower().strip(" ")
    flag = 0
    if isAlphabetic(cipher) and isAlphabetic(key):
        # trường hợp mã hoá bằng với key
        if len(cipher) == len(key):
            # Việc giải mã đơn giản, không cần phải chèn plain text đã giải được vào key
            for i in range(0, len(key)):
                pos = (alphabet.find(cipher[i])-alphabet.find(key[i]) % 26)
                plaintext = plaintext+alphabet[abs(pos)]
        elif len(key) < len(cipher):
            # Vì chiều dài plain text bằng với chiều dài cipher,
            # nên nếu chiều dài bằng nhau là lúc giải mã xong
            while len(plaintext) < len(cipher):
                # biến flag giúp cho việc sau mỗi vòng lặp,
                # phần tử thứ i sẽ quay về đúng vị trí của nó
                for i in range(flag, len(cipher)):
                    # lấy vị trí của phần tử thứ i
                    pos = (alphabet.find(cipher[i])-alphabet.find(key[i])) % 26
                    # chèn phần tử thứ i vào chuỗi
                    plaintext = plaintext + alphabet[abs(pos)]
                    # chèn phần tử thứ i sau khi giải mã xong vào key
                    key = key + plaintext[i]
                    flag = flag+1
                    print('Plain text in position',i+1,':',cipher[i],'=',plaintext[i])
                    print('key in position',i+1,':',key[i])

            print()
            print('Cipher:', ori_cipher)
            print('Key:', ori_key)
            print('Decrypt:', plaintext)
        else:
            print('Cipher text must shorter than key!')
    else:
        print('A character out of space of key')


while True:
    print()
    chon = input('1. Encode\n2. Decode\nChon: ')
    if chon == '1' or chon == '2':
        os.system('clear')
        if chon == '1':
            # Nhập các thông tin mã hoá và key
            print('____________Encode______________\n')
            plaintext = input('Input plain text: ')
            key = input('Input key: ')
            encode(plaintext, key)
        if chon == '2':
            print('____________Decode______________\n')
            # Nhập các thông tin và key
            cipher = input('Input cipher text: ')
            key = input('Input key: ')
            decode(cipher, key)
    else:
        print('Select again!')
        print()

# The program that encrypts text using Caesar Cipher


def encrypt_caesar_cipher(s, n):
    alphabet_big_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_small_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_big_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_small_en = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    for i in range(len(s)):
        if s[i] not in alphabet_big_ru and s[i] not in alphabet_small_ru and s[i] not in alphabet_big_en and s[i] not in alphabet_small_en:
            new_s += s[i]
        elif s[i] in alphabet_big_ru:
            for j in range(len(alphabet_big_ru)):
                if s[i] == alphabet_big_ru[-j]:
                    new_s += alphabet_big_ru[-j + n]
        elif s[i] in alphabet_small_ru:
            for j in range(len(alphabet_small_ru)):
                if s[i] == alphabet_small_ru[-j]:
                    new_s += alphabet_small_ru[-j + n]
        elif s[i] in alphabet_big_en:
            for j in range(len(alphabet_big_en)):
                if s[i] == alphabet_big_en[-j]:
                    new_s += alphabet_big_en[-j + n]
        elif s[i] in alphabet_small_en:
            for j in range(len(alphabet_small_en)):
                if s[i] == alphabet_small_en[-j]:
                    new_s += alphabet_small_en[-j + n]

    return new_s


text = input()
k = int(input())
print(encrypt_caesar_cipher(text, k))
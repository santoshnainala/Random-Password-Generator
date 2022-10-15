#Random password generator
import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
while True:
    pass_len=int(input())
    password=""
    for i in range(0,pass_len):
        pass_char = random.choice(chars)
        password+=pass_char
    print("Random password:",password)

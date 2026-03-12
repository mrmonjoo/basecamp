import random

codes = []

for i in range(4):
    codes.append(random.randint(0, 9))
# print(codes)

guess = input("BREACH ATTEMPT> ")
# print(guess)

for digit in guess:
    print(digit)

guess_list = []

for digit in guess:
    guess_list.append(int(digit))

print(guess_list)
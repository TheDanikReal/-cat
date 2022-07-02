import random
numberrandom = random.randint(1, 5)
mynumber = input(Угадай число от 1 до 5: )
if numberrandom == mynumber:
  print("Ты угадал!")
else:
  print(f"Ты не угадал! \nравильное число было: {numberrandom}")
print("надеюсь тебе понравилось)

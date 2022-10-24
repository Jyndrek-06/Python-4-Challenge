from random import randint
def game():
  import random
  secret = random.randint(1, 101)
  count = 0
  while True:
    num = int(input("Choose number:"))
    if num <= 1 or num >= 101:
      print("You have chosen a number that is out of play!")
      count += 1

    if num < secret:
      print("Wrong number! You chose a lower number than the secret number.")
      count += 1

    if num > secret:
      print("Wrong! You chose a number greater than the secret number.")
      count += 1
   
    if num == secret:
       print(f"You won and it took {count} tries")
       break
    elif count == 8:
       print("Sorry, you ran out of tries!")
       break

    
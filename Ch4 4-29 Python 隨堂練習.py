import random
num = random.randint(1,10) #Randomly generate a number between 1 to 10
answer = -1 #answer
while answer != num:
  answer = eval(input("Please guess a number between 1 to 10:"))
  if answer > num:
    print("The number you entered is too large.")
  if answer < num:
    print("The number you entered is too small.")
  else:
   print("Congratulations!")

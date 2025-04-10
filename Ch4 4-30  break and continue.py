answer = input("英語で「ナマケモノ」と入力してください：")
while answer.upper() != "SLOTH":
 if answer.upper() == "QUIT":
  print("Closed.")
  break
 answer = input("間違った答えです。「ナマケモノ」の英語の単語をもう一度入力してください：")
else:
 print("You got it right!")
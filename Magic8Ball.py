#Magic8Ball.py
#Name:Alexa Falkner
#Date:9/7/2025
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
question = input ("What is your question? ")
answer = ["Concentrate and ask again.", "Yes. Wait actually NO.","Don't count on it.","Very Doubtful.",
          "Absolutely NOT.","Uhh yes!","I don't care."]
length = len(answer)
r = random.random() * length

r = int(r) 
response = answer [r]
print(response)
  #Answer question randomly with one of the options from your earlier list.


if __name__ == '__main__':
  main()

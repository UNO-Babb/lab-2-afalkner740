#FutureTime.py
#Name:Alexa Falkner
#Date:9/7/2025
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
def main():
  import datetime
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute
  print(currentHour , currentMinute)
 #this is just for checking, we should delete it later
  #TODO:
  #Ask user for hours
  hours  = int(input("What hours from 0-24? "))
  #Ask user for minutes
  minutes = int (input ("What minutes from 0-60? "))
  #Calculate the time after the user-supplied time has passed.
  futurehours = (currentHour + hours) % 24
  futureMins = (currentMinute + minutes) % 60
  print(futurehours ,futureMins)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()

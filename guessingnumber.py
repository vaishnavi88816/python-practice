import random 
num=random.randint(1,10)
tries=0
while True:
   guess=int(input("please give your number between 1 to 10:-"))
   if num==guess:
      tries+=1
      print(f"you are right  you guess the number in {tries}tries")
      break
   elif num>=guess:
      tries+=1
      print("go a little higher")
   elif num<=guess:
      tries+=1
      print("go a little lower")
   else:
      tries+=1
      print("sorry u are wrong")
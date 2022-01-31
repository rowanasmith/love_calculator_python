# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name_string = name1.lower() + name2.lower()

t = lower_name_string.count("t")
r = lower_name_string.count("r")
u = lower_name_string.count("u")
e = lower_name_string.count("e")
l = lower_name_string.count("l")
o = lower_name_string.count("o")
v = lower_name_string.count("v")

digit_one = str(t + r + u + e)
digit_two = str(l + o + v + e)
result = int(digit_one + digit_two)

if result < 10 or result > 90:
  print(f"Your score is {result}, you go together like Coke and Mentos.")
elif result >= 40 and result <= 50:
  print(f"Your score is {result}, you are alright together")
else:
  print(f"Your score is {result})
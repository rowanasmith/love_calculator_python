# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name_string = lower(name1 + name2)

t = lower_name_string.count("t")
r = lower_name_string.count("r")
u = lower_name_string.count("u")
e = lower_name_string.count("e")
l = lower_name_string.count("l")
o = lower_name_string.count("o")
v = lower_name_string.count("v")

digit_one = string(t + r + u + e)
digit_two = string(l + o + v + e)
result = int(digit_one + digit_two)

print(result)
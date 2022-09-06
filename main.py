import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

number_of_names = len(names)
 
random_name = random.randint(0, number_of_names - 1)

buyer = names[random_name]

#line below is a shorter way of writing this code
#buyer = random.choice(names)  

print(buyer + " is going to buy the meal today!")


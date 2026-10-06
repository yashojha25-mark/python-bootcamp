# p1 = 10
# p2 = 20

# val = p1 < p2

# print(val)

# print(type(val))

"""Marks comparison"""

# s1 = int(input("Enter marks of Student 1: "))
# s2 = int(input("Enter marks of Student 2: "))

# print("Are the marks equal?", s1 == s2)

# print("Is Student 1 higher?", s1 > s2)
# print("Is Student 2 higher?", s2 > s1)


"""E-commerce bill calculation"""
# base_delivery_fee = 25
# item_total = 420
# surge_fee = 15

# final_bill = item_total + base_delivery_fee + surge_fee

# print("Item Total:", item_total)
# print("Delivery Fee:", base_delivery_fee)
# print("Surge Fee:", surge_fee)
# print("Final Bill:", final_bill)

# gold_member = True

# free_delivery = gold_member and item_total > 500

# print("Eligible for Free Delivery:", free_delivery)


"""Mangoes and Rice Boxes"""
# mangoes = 138

# full_boxes = mangoes // 12
# left_mangoes = mangoes % 12

# print("Full dozen boxes:", full_boxes)
# print("Leftover mangoes:", left_mangoes)

# rice_kg = 45
# rice_grams = rice_kg * 1000

# full_bags = rice_grams // 5
# left_grams = rice_grams % 5

# print("Full 5g bags:", full_bags)
# print("Leftover rice:", left_grams, "g")

"""If-Else Statements"""
# is_shop_open = False

# print("4")

# if (is_shop_open == True):
#     print("1")
#     print("2")
# else:
#     print("0")

# print("200")

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

"""If-Elif-Else Ladder"""

# age = int(input("Enter your age: "))

# if (age <= 10):
#     print("Child")
# elif (age <= 20):
#     print("Teenager")
# elif (age <= 60):
#     print("Adult")
# else:
#     print("Senior Citizen")

"""Nested If-Else Statements"""

# is_gate_open = True
# has_validID = True

# if(is_gate_open == True):
#     if(has_validID == True):
#         print("Welcome to the event!")
#     else:
#         print("Please show a valid ID.")
# else:
#     print("The gate is closed. Please come back later.")


# is_lightning_member = True
# cart_value = int(input("Enter the cart value: "))
# is_raining = True

# if is_lightning_member and cart_value > 199:
#     print("Free Delivery")

# elif is_raining and cart_value < 299:
#     print("Heavy Rain Surge - Delivery Fee: ₹49")

# elif cart_value >= 300 and cart_value <= 600:
#     print("Delivery Fee: ₹15")

# else:
#     print("Standard Delivery Fee: ₹25")


"""While Loop"""

# count = int(input("Enter the number of items: "))

# if count == 5:
#     print("5")
#     print("4")
#     print("3")
#     print("2")
#     print("1")
#     print("Happy New Year!")

# elif count == 10:
#     print("10")
#     print("9")
#     print("8")
#     print("7")
#     print("6")
#     print("5")
#     print("4")
#     print("3")
#     print("2")
#     print("1")
#     print("Happy New Year!")

# timer = int(input("Enter the countdown timer value: "))
# resp = 1
# maxlimit = 10

# while resp != 0:
#     print(timer)
#     resp = int(input("Enter 0 to exit: "))
#     timer -= 1
    # maxlimit -= 1
#     if (maxlimit >= 0):
#         print("Max limit reached")
#        
#         break
# print("Outside while loop")

"""For Loop"""

# for number in range(2, 21, 2):
#     print(number)


# items = ["Apple", "Banana", "Mango", "Orange"]

# for item in items:
#     print(item)


# prizes = [100, 250, 500, 150, 300]

# total = 0
# count = 0

# for prize in prizes:
#     total += prize
#     count += 1

# print("Total:", total)
# print("Count:", count)

# Prime Numbers......

# for number in range(2, 51):
#     count = 0
#     for divisor in range(1, number + 1):
#         if number % divisor == 0:
#             count += 1

#     if count == 2:
#         print(number)


# Fibonacci sequence......
# a, b = 0, 1
# count = 0

# while count < 10: 
#     print(a)
#     a, b = b, a + b
#     count += 1


# Question -1 Myntra Shopping Discount Cart

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))

subtotal = item1 + item2
discount = subtotal * 15 / 100
delivery_fee = 99
total = subtotal - discount + delivery_fee

print("Item 1: ", item1)
print("Item 2: ", item2)
print("Subtotal: ", subtotal)
print("Promo Discount (15%): ", discount)
print("Delivery Fee: ", delivery_fee)
print("Final Total: ", total)


# Question-2 Café Outing Split-Bill Calculator

bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))

tip = bill * 10 / 100
total_bill = bill + tip
each_person = total_bill / friends

print("Original Bill: ", bill)
print("Tip (10%): ", tip)
print("Total Bill: ", total_bill)
print("Each Person Pays: ", each_person)


# Question-3 Instagram Reel Engagement Tracker

views = int(input("Enter number of views: "))
likes = int(input("Enter number of likes: "))
comments = int(input("Enter number of comments: "))

engagement_rate = ((likes + comments) / views) * 100

print("Views:", views)
print("Likes:", likes)
print("Comments:", comments)
print("Engagement Rate:", engagement_rate, "%")


#Question-4 Monthly Allowance & Savings Planner

pocket_money = float(input("Enter your monthly pocket money: "))

canteen = float(input("Enter canteen expense: "))
transport = float(input("Enter transport expense: "))
shopping = float(input("Enter shopping expense: "))

total_expenses = canteen + transport + shopping
savings = pocket_money - total_expenses

is_budget_safe = savings >= 0

print("Pocket Money: ", pocket_money)
print("Canteen Expense: ", canteen)
print("Transport Expense: ", transport)
print("Shopping Expense: ", shopping)
print("Total Expenses: ", total_expenses)
print("Remaining Savings: ", savings)
print("Is Budget Safe:", is_budget_safe)
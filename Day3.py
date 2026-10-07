# IRCTC Ticket Eligibility

age = int(input("Enter age: "))
gender = input("Enter gender: ")
alone = input("Are you traveling alone? (yes/no): ")
tatkal = input("Is it a Tatkal ticket? (yes/no): ")
holiday = input("Is it a blackout holiday? (yes/no): ")

if (age >= 60 or (gender == "female" and alone == "yes")) and tatkal == "no" and holiday == "no":
    print("Eligible for lower berth preference and discount.")
else:
    print("Not eligible.")
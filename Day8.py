
"""Problem: Library late fee calculator"""

def cal_fine(late_days, book_type="standard", premium=False):
    
    if book_type == "standard":
        if late_days <= 5:
            fine = late_days * 5
        else:
            fine = (5 * 5) + ((late_days - 5) * 10)

    elif book_type == "reference":
        fine = late_days * 20
    else:
        return "Invalid book type"
    if premium:
        fine = fine - (fine * 20 / 100)

    return fine

print(cal_fine(3))
print(cal_fine(8))
print(cal_fine(4, "reference"))
print(cal_fine(8, "standard", True))
print(cal_fine(5, "reference", True))


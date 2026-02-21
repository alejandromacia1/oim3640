
#score = int(input("Enter your score: "))

# if score >= 60:
#     print("Congratulations! You passed the exam")
# elif score >= 90:
#     print("Excellent work! You scored an A")
# else:
#     print("Unfortunately, you did not pass. Better luck next time.")

# if score >= 90:
#     print("Excellent work! You scored an A")
# if score >= 60:
#     print("Congratulations! You passed the exam.")
# else:
#     print("Unfortunately, you did not pass. Better luck next time.")

# def evaluate_score(score):
#     if score >= 90:
#         return "Excellent work! You scored an A"
#     elif score >= 60:
#         return "Congratulations! You passed the exam."
#     else:
#         return "Unfortunately, you did not pass. Better luck next time"

#the difference between print and return is that print will print both, and retun will end the function immediately. 

# def mystery(x):
#     if x > 0:
#         return "positive"
#     else:
#         return "non-positive"
#     print ("done")

# result = mystery(0)
# print(result)

# x = 15 
# y = x > 10 and x < 200
# print(type(y))
# print(y)

# def is_leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     return False

# print(is_leap_year(2026))
# print(is_leap_year(2024))
# print(is_leap_year(2028))

#how to find the next leap year after a given year?

# def check(n):
#     if n % 2 == 0:
#         if n % 3 == 0:
#             print("A")
#         else:
#             print("B")
#     else: 
#         print("C")

# check(8)
# check(6)

def check(n):
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} is divisible by both 2 and 3")
    elif n % 2 == 0:
        print(f"{n} is divisible by 2 but not 3")
    else:
        print(f"{n} is not divisible by 2")

check(8)
check(6)
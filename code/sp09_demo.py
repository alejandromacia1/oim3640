
# for i in range(5):
#     print(i)

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# response = ""
# while response != "quit":
#     response = input("Enter command: ")
#     print(f"You said: {response}")

# arrival_time = ""
# while arrival_time != "quit":
#     arrival_time = input("Enter your arrival time (or 'quit' to exit): ")
#     if arrival_time != "quit":
#         print(f"You arrived at: {arrival_time}")
#         if arrival_time < "09:45":
#             print("You are early!")
#         elif arrival_time == "09:45":
#             print("You are on time!")
#         else:
#             print("You are late!")

#break: breaks the loop entirely. 

# Example: Simple Login System
# print("\n--- Simple Login System ---")
# username = "admin"
# password = "password123"

# while True:
#     user_input = input("Enter username: ")
#     pass_input = input("Enter password: ")

#     if user_input == username and pass_input == password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid username or password. Try again.")


# # creating a game loop
# def game_loop():
#     print("game on...")
#     return "game over"

# while True:
#     result = game_loop()
#     if result == "game over":
#         break


# break - exit the loop immediately
# words = ["hello", "world", "target", "python"]
# for w in words:
#     print('checking:', w)
#     if w == "target":
#         print("Found it!")
#         break


# words = ["hello", "world", "target", "python"]
# for w in words:
#     print('Checking:', w)
#     if w == "target":
#         print("Found it!\n")
#         continue
#     print("Not the target\n")

# continue - skip to the next iteration
# for num in range(10):
#     if num % 2 == 0:
#         continue
#     print(num)  # prints odd numbers only


def f(n):
    for num in range(n):
        if num % 2 == 0:
            continue
        return num


# print(f(10))
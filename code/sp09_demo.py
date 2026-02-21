
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

arrival_time = ""
while arrival_time != "quit":
    arrival_time = input("Enter your arrival time (or 'quit' to exit): ")
    if arrival_time != "quit":
        print(f"You arrived at: {arrival_time}")
        if arrival_time < "09:45":
            print("You are early!")
        elif arrival_time == "09:45":
            print("You are on time!")
        else:
            print("You are late!")
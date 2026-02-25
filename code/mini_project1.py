
print("Welcome to Professor Li's restaurant guide!")

#User Preferences
cuisine = input("What type of cuisine are you in the mood for? (Select one: French, Italian, Mexican): ")

while True:
    vibe = input("What vibe do you want? (Casual, Romantic, Fancy): ")
    budget = input("What budget are you working with? ($, $$, $$$): ")

    if vibe == "Fancy" and budget == "$":
        print("Fancy dining requires at least $$ budget. Please choose again.")

    elif vibe == "Casual" and budget == "$$$":
        print("Casual dining is not typically $$$. Please choose again.")

    else:
        break

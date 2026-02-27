
print("Welcome to Professor Li's restaurant guide!")

#User Preferences
cuisine = input("\nWhat type of cuisine are you in the mood for? (Select one: French, Italian, Mexican): ")

while True:
    vibe = input("\nWhat vibe do you want? (Casual, Romantic, Fancy): ")
    budget = input("\nWhat budget are you working with? ($, $$, $$$): ")

    if vibe == "Fancy" and budget == "$":
        print("Fancy dining requires at least $$ budget. Please choose again.")

    elif vibe == "Casual" and budget == "$$$":
        print("Casual dining is not typically $$$. Please choose again.")

    else:
        break

#Restaurant Recommendations.
#Cuisine Preference
if cuisine == "French":
    restaurant = "French Bistro"
elif cuisine == "Italian":
    restaurant = "Italian Trattoria"
elif cuisine == "Mexican":
    restaurant = "Mexican Grill"
else:
    restaurant = "No Restaurant Found"

#Vibe Preference
if vibe == "Casual":
    restaurant = "Casual " + restaurant
elif vibe == "Romantic":
    restaurant = "Signature " + restaurant
elif vibe == "Fancy":
    restaurant = "Premium " + restaurant


#Budget Preference (Multiplier Strategy)
if budget == "$":
    multiplier = 1
elif budget == "$$":
    multiplier = 1.4
else:
    multiplier = 2.2

#Tailored Recommendation based on User Inputs 
print("Based on your preferences, we highly recommend:", restaurant)

#Menu Offerings - French
if cuisine == "French":
    entree1 = "Onion Soup"
    entree2 = "Salad Nicoise"
    entree_price1 = 9
    entree_price2 = 12

    main1 = "Coq au Vin"
    main2 = "Steak Frites"
    main_price1 = 18
    main_price2 = 21

    dessert1 = "Macarons"
    dessert2 = "Creme Brulee"
    dessert_price1 = 6
    dessert_price2 = 7

elif cuisine == "Italian":
    entree1 = "Caprese Salad"
    entree2 = "Bruschetta"
    entree_price1 = 9
    entree_price2 = 10

    main1 = "Margherita Pizza"
    main2 = "Gnocchi alla Sorrentina"
    main_price1 = 16
    main_price2 = 19

    dessert1 = "Tiramisu"
    dessert2 = "Cannoli"
    dessert_price1 = 8
    dessert_price2 = 5

elif cuisine == "Mexican":
    entree1 = "Guacamole and Chips"
    entree2 = "Esquites"
    entree_price1 = 8
    entree_price2 = 6

    main1 = "Chilaquiles"
    main2 = "Tacos al Pastor"
    main_price1 = 11
    main_price2 = 10

    dessert1 = "Tres Leches Cake"
    dessert2 = "Churros"
    dessert_price1 = 6
    dessert_price2 = 5

#Pricing Mechanisms
entree_price1 *= multiplier
entree_price2 *= multiplier
main_price1 *= multiplier
main_price2 *= multiplier
dessert_price1 *= multiplier
dessert_price2 *= multiplier

print("\n----- ENTREE -----")
print("1.", entree1, "- $", round(entree_price1, 2))
print("2.", entree2, "- $", round(entree_price2, 2))
entree_choice = int(input("Select the entree of your choice (1 or 2): "))

print("\n----- MAIN COURSE -----")
print("1.", main1, "- $", round(main_price1, 2))
print("2.", main2, "- $", round(main_price2, 2))
main_choice = int(input("Select the main course of your choice (1 or 2): "))

print("\n----- DESSERT -----")
print("1.", dessert1, "- $", round(dessert_price1, 2))
print("2.", dessert2, "- $", round(dessert_price2, 2))
dessert_choice = int(input("Select the dessert of your choice (1 or 2): "))

#Calculate Tax (Massachusetts):
def calc_tax(price):
    """Calculate product tax based on given price."""
    tax_rate = 0.0625  # Massachusetts tax rate (6.25%)
    tax = price * tax_rate
    return tax

#Conditions - Overview of Customer Decisions
if entree_choice == 1:
    decision_entree = entree1
    decision_entree_price = entree_price1
else:
    decision_entree = entree2
    decision_entree_price = entree_price2

if main_choice == 1:
    decision_main = main1
    decision_main_price = main_price1
else:
    decision_main = main2
    decision_main_price = main_price2

if dessert_choice == 1:
    decision_dessert = dessert1
    decision_dessert_price = dessert_price1
else:
    decision_dessert = dessert2
    decision_dessert_price = dessert_price2

    #Calculating Massachusetts Tax
def calc_tax(price):
    """Calculate product tax based on given price."""
    tax_rate = 0.0625  # tax rate in Massachusetts (6.25%)
    tax = price * tax_rate
    return tax

#Calculating Totals (tax is always included, tip is optional but highly suggested)
subtotal = decision_entree_price + decision_main_price + decision_dessert_price

tax = calc_tax(subtotal)

tip = 0
tip_rate = 0

add_tip = input("\nWould you like to add a tip? (yes/no): ").strip().lower()

if add_tip == "yes":

    while True:
        print("\nSelect tip rate:")
        print("1. 18%")
        print("2. 20% (Suggested Amount)")
        print("3. 22%")

        tip_choice = input("Choose 1, 2, or 3: ").strip()

        if tip_choice == "1":
            tip_rate = 0.18
            break
        elif tip_choice == "2":
            tip_rate = 0.20
            break
        elif tip_choice == "3":
            tip_rate = 0.22
            break
        else:
            print("No tip selected.")

    tip = subtotal * tip_rate

total = subtotal + tax + tip

print("\n----- CUSTOMER RECEIPT -----")
print("\nRestaurant:", restaurant)
print("\nServer: Alejandro Macia")

print("\nItems:")
print(f"Entree: {decision_entree} - ${decision_entree_price:.2f}")
print(f"Main: {decision_main} - ${decision_main_price:.2f}")
print(f"Dessert: {decision_dessert} - ${decision_dessert_price:.2f}")

print("\nCharges:")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6.25%): ${tax:.2f}")

if add_tip == "yes" and tip_rate > 0:
    print(f"Tip ({int(tip_rate*100)}%): ${tip:.2f}")
else:
    print("Tip: $0.00")

print("===================")
print(f"TOTAL:    ${total:.2f}")
print("===================")

print("\nThank you for visiting Professor Li's restaurant! We hope you have a nice day")

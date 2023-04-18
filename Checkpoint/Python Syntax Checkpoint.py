def get_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print(f"\nInvalid input. Please enter one of {valid_inputs}")

print("Welcome to Python Pizza Deliveries!\n")
pizza_size = get_input("\nWhat size of pizza do you want?\nPlease enter S for small, M for medium, and L for Large: ", ["S", "M", "L"])
add_pepperoni = get_input("\nDo you want pepperoni? Please enter Y or N: ", ["Y", "N"])
extra_cheese = get_input("\nDo you want extra cheese? Please enter Y or N: ", ["Y", "N"])

bill = 0
if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    bill += 2 if pizza_size == "S" else 3

if extra_cheese == "Y":
    bill += 1

print(f"\nYour final bill is ${bill}.")
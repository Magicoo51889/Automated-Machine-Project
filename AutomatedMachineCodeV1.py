import time

entrances = 0


def add_entrance(entrances):
    if entrances <= 500:
        entrances += 1  # adds one to the variable entrances
    else:
        print("Sorry but the park is currently at maximum capacity. We are sorry for any inconvenience.")
    return entrances


def welcome():
    print("Welcome to Copington Adventure Theme Park")  # prints welcome message
    time.sleep(1)
    surname = input("What is your surname? ")
    if surname == "admin":
        admin()
    else:
        print("Hello", surname)
    return surname


def admin():
    which_price_change = input("What price would you like to change? (type 'exit' to leave console) ")
    if which_price_change == "exit":
        return None  # doesn't return anything. It exits the code with no return value
    elif which_price_change == int:
        print("Sorry but that price does not exist, restart program if you want to retry ")
        return None
    new_price = int(input("Enter new price: "))

    if which_price_change == "adult_price":
        CurrentPrices.adult_price = new_price
        return CurrentPrices.adult_price

    if which_price_change == "child_price":
        CurrentPrices.child_price = new_price
        return CurrentPrices.child_price

    if which_price_change == "senior_price":
        CurrentPrices.senior_price = new_price
        return CurrentPrices.senior_price

    if which_price_change == "student_price":
        CurrentPrices.student_price = new_price
        return CurrentPrices.student_price

    if which_price_change == "wristband_price":
        CurrentPrices.wristband_price = new_price
        return CurrentPrices.wristband_price

    else:
        print("Sorry but that price does not exist, restart program if you want to retry")  # could implement a while
        # loop till the admin inputs something valid


class CurrentPrices:  # sets variables prices
    adult_price = int(20)
    child_price = int(12)
    senior_price = int(11)
    student_price = int(11)
    wristband_price = int(20)


def list_price():  # prints what is in the quote and then variables of the prices so that they can be updated
    print("The prices for one adult is: ", CurrentPrices.adult_price)
    print("The prices for one adult is: ", CurrentPrices.child_price)
    print("The prices for one adult is: ", CurrentPrices.senior_price)
    print("The prices for one adult is: ", CurrentPrices.student_price)


def cost(num_adult, num_child, num_senior, num_student, num_wristband):
    total_cost = int((
            num_adult * CurrentPrices.adult_price + num_child * CurrentPrices.child_price + num_senior *
            CurrentPrices.senior_price + num_student * CurrentPrices.student_price + num_wristband * CurrentPrices.
            wristband_price))  # calculates the total cost of the tickets
    print("This costs £", total_cost)  # says the cost
    proceed = input(
        "If you want to proceed to checkout type Yes, else type No. ")  # informs the user of
    # the price then asks if they want to confirm the number of tickets and the price.
    if proceed == "yes" or "Yes":
        return total_cost  # returns the number of entrances and the total cost of the ticket
    else:
        cost(num_adult, num_child, num_senior, num_student, num_wristband)


def parking_pass():
    parking_pass_wanted = input("Do you want a parking pass? ")
    if parking_pass_wanted == "yes" or "Yes":
        parking = True
        return parking
    else:
        parking = False
        return parking


def payment():
    payment_method = input("How would you like to pay? ")
    if payment_method == "Card" or " card" or "debit card" or "Debit card":  # if they type something in differently it
        # is accommodated
        print("Please pay via contactless (up to £45) or using your pin ")  # no change due
        time.sleep(5)
    elif payment_method == "cash" or "Cash" or "Coins" or "coins":
        print("Please play using coins or cash. If using cash only use £10 or £20 notes")
        time.sleep(5)
    else:
        print("That is not a valid payment method, sorry.")  # rejects other unknown methods of payment


def print_ticket(num_adults, num_child, num_senior, num_students, num_wristbands):
    print("Printing ticket. Please wait.")
    # representation of the ticket
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Local time:", local_time)  # this imports the local time onto the ticket
    print(num_adults)
    print(num_child)
    print(num_senior)
    print(num_students)
    print(num_wristbands)
    time.sleep(2)  # wait for 2 seconds
    print("Thank you for coming to Copington Adventure Theme Park, please enjoy your visit!")


def print_parking(parking):
    if parking is True:
        print("Printing parking pass. Please wait.")
        time.sleep(2)


# calling the functions separate from the rest of the code:

add_entrance(entrances)

welcome()

list_price()

num_adult = int(input("How many adults there? "))
num_child = int(input("How many children are there? "))
num_senior = int(input("How many seniors are there? "))
num_student = int(input("How many students are there? "))
num_wristband = int(input("How many wristbands would you like? "))

cost(num_adult, num_child, num_senior, num_student, num_wristband)

parking_pass()

payment()

print_ticket(num_adults, num_child, num_senior, num_students, num_wristbands)

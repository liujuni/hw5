from Selections import Nearby, Refi, ExtraPay, OilChange

def main_menu():
    print("Welcome to Auto Payment Savor!")

    while True:
        display_msgs()
        user_input = input()

        if user_input == 'exit':
            break

        elif user_input == '1':
            print()
            print("Enter your current and new car loan info...")
            print("Loan Amount:", end=" ")
            loan_amount = float(input())
            print("Current Rate:", end=" ")
            current_rate = float(input())
            print("Current Terms:", end=" ")
            current_terms = float(input())
            print("New Rate:", end=" ")
            new_rate = float(input())
            print("New Terms:", end=" ")
            new_terms = float(input())
            print("Any Application Fees:", end=" ")
            app_fees = float(input())
            print("Enter 'ok' to proceed:", end=" ")
            okay = input()

            if okay == 'ok':
                refi_1 = Refi(loan_amount, current_rate, current_terms, new_rate, new_terms, app_fees)
                c_payment = refi_1.get_current_payment()
                n_payment = refi_1.get_new_payment()
                print()
                print("Here is the refi summary...")
                print("Your current monthly payment is:", end=" $")
                print(c_payment)
                print("Your NEW monthly payment will be:", end=" $")
                print(n_payment)
                print()
                print("You will save:", end=" $")
                print(c_payment - n_payment)
                print()
            else:
                print("Invalid user input.")
                print()

        elif user_input == '2':
            print()
            print("Enter your current car loan info...")
            print("Loan Amount:", end=" ")
            loan_amount = float(input())
            print("Loan Rate:", end=" ")
            loan_rate = float(input())
            print("Loan Terms:", end=" ")
            loan_terms = float(input())
            print("Extra Payment to the Principal:", end=" ")
            extra_payment = float(input())
            print("Enter 'ok' to proceed:", end=" ")
            okay = input()

            if okay == 'ok':
                extra_pay_1 = ExtraPay(loan_amount, loan_rate, loan_terms, extra_payment)
                print("Here is the summary for making an extra payment towards principal...")
                print("You will be saving this much over the entire terms:", end=" $")
                print(extra_pay_1.get_savings())
                print()
            else:
                print("Invalid user input.")
                print()

        elif user_input == '3':
            print()
            print("Searching for oil change estimates from nearby authorized dealerships...")
            print("Please enter '10' or '25' or '50' for the searching radius:", end=" ")
            radius = input()
            avg_cost = 0

            if radius == '10':
                dealerships = Nearby(400, 525, 2)
                avg_cost = dealerships.get_avg()
            elif radius == '25':
                dealerships = Nearby(400, 525, 4)
                avg_cost = dealerships.get_avg()
            elif radius == '50':
                dealerships = Nearby(400, 525, 7)
                avg_cost = dealerships.get_avg()

            print("What is the cost for engine oil you purchased?", end=" ")
            material_cost = float(input())
            print("Approximately, how many miles do you drive per year?", end=" ")
            mileage = float(input())
            print("Enter 'ok' to proceed:", end=" ")
            okay = input()

            if okay == 'ok':
                oil_change_1 = OilChange(avg_cost, material_cost, mileage)
                print("Here is the savings summary for DIY oil change...")
                print("You will be saving this much per year by performing DIY oil change:", end=" $")
                print(oil_change_1.get_savings())
                print()
            else:
                print("Invalid user input.")
                print()

        else:
            print("Please try again and enter a correct selection number!")
            print()


def display_msgs():
    intro_msg = "What would you like to do? Please select one of the followings:"
    msg_1 = "Enter '1' to find out savings from refinancing your auto loan."
    msg_2 = "Enter '2' to find out savings from making an extra payment towards principal."
    msg_3 = "Enter '3' to find out savings from performing DIY oil change."
    exit_msg = "Type 'exit' to exit out the program."

    script = list()
    script.append(intro_msg)
    script.append(msg_1)
    script.append(msg_2)
    script.append(msg_3)
    script.append(exit_msg)

    for i in script:
        print(i)


if __name__ == "__main__":
    main_menu()

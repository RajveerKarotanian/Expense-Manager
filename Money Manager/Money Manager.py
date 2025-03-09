"""
Name: Rajveer Karotanian
    
Date: 11/24/24

Problem Description:    The program to be created must act as a manager of the user's income/expenses, letting
                        the user add transactions, view their transactions, calculate the total incomes/expense,
                        and load/save their transactions to/from a file. When the program is executed, it must give
                        the user the options to perform any of the mentioned tasks, where an error is displayed 
                        when they do not enter a given option. When choosing to add a transaction, the user must
                        pick the type of transaction: income or expense, where they must be prompted for an amount 
                        after. An error must be displayed if the user enters incorrect information. When choosing to
                        view transactions, the list of transactions must be displayed to the user in a user-friendly
                        manner. When choosing to calculate totals, the program must calculate the total income,
                        total expense, and net total, displaying all the values to the user. When choosing to load
                        transactions, the program must load the transactions from the file. When choosing to save
                        transactions, the program must save transactions to a text file, where the user needs to be 
                        given the option to either add onto the contents of the file, or overwrite them completely.
                        The final option the user should be given is to exit the program. Whenever an error is
                        displayed, it must be given to the user in a clear manner, and then they need to be able
                        to reenter the prompted information.
"""


# Function to add transaction
def add_transaction(transactions):
    # Ask user for transaction type until a valid type is entered
    while True:
        trans_type = input(
            "\nPlease enter the type of transaction (Income or Expense): "
        ).capitalize()
        # Display error if invalid choice is entered and ask user to reenter their choice
        if trans_type != "Income" and trans_type != "Expense":
            print("\nInvalid type! Please enter a valid type.")
        else:
            break
    # Ask user for transaction amount until valid amount is entered
    while True:
        trans_amt = input("\nPlease enter the transaction amount: ")
        # Display error if invalid choice is entered and ask user to reenter their choice
        try:
            trans_amt = float(trans_amt)
            break
        except:
            print("\nInvalid amount! Please enter a valid number.")
    # Add transaction to list
    transactions.append({"Type": trans_type, "Amount": trans_amt})
    print("\nTransaction added successfully")


# Function to display transactions
def display_transactions(transactions):
    if transactions == []:  # If user has no transactions
        print("\nYou have no transactions.")
    else:
        # Display transactions in a user-friendly manner
        print("")
        # iterate through transactions and display each one to user
        for x in transactions:
            print(
                "Type:",
                x["Type"],
                "\tAmount: $" + str(format(x["Amount"], ".2f")),
            )


# Function to calculate and display total income and expense
def calculate(transactions):
    total_income = 0
    total_expense = 0
    # iterate through transactions to sum up individual totals
    for x in transactions:
        if x["Type"] == "Income":
            total_income += x["Amount"]
        else:
            total_expense += x["Amount"]
    # Display totals
    print(
        "\nTotal Income: $" + str(format(total_income, ".2f")),
        "\nTotal Expense: $" + str(format(total_expense, ".2f")),
    )
    print("Net Total: $" + str(format(total_income - total_expense, ".2f")))


# Function to load transactions from text file
def load(transactions):
    # Open file to read
    with open("transactions.txt", "r") as my_file:
        # go through file line by line
        for line in my_file:
            # split the components of the line and add it onto the current list of transactions
            line_split = line.split()
            transactions.append(
                {
                    "Type": line_split[1],
                    "Amount": float(line_split[3].replace("$", "")),
                }
            )
        print("\nTransactions loaded!")


# Function to save transactions to text file
def save(transactions):
    # Ask user if they would like to add to file or overwrite it
    while True:
        mode = input(
            "\nWould you like to [add] to previous transactions or [overwrite] them?: "
        )
        # Display error if invalid choice is entered and ask user to reenter their choice
        if mode.lower() != "add" and mode.lower() != "overwrite":
            print("\nInvalid choice! Please pick [add] or [overwrite].")
        else:
            # convert answer to a valid mode for the open() function
            if mode.lower() == "add":
                mode = "a"
            else:
                mode = "w"
            break
    # Open file and write to it
    with open("transactions.txt", mode) as my_file:
        # iterate through list and write each individual transaction to file
        for x in transactions:
            my_file.write(
                "Type: "
                + str(x["Type"])
                + "\tAmount: $"
                + str(format(x["Amount"], ".2f"))
                + "\n"
            )
    print("\nTransactions saved!")


# Greet user to program
print("Welcome to the Money Manager!")

# Create list to store transactions
transactions = []

# Infinite loop to allow user to keep selecting options as many times as they wish
while True:
    # Let user pick what they would like to do
    choice = input(
        "\nPlease pick an option:\n1: Add Transaction\n2: View Transactions\n3: Calculate Totals\n4: Load Transactions\n5: Save Transactions\n6: Exit\n\nChoice: "
    )
    # Run code based on choice picked
    if choice == "1":
        add_transaction(transactions)
    elif choice == "2":
        display_transactions(transactions)
    elif choice == "3":
        calculate(transactions)
    elif choice == "4":
        load(transactions)
    elif choice == "5":
        save(transactions)
    elif choice == "6":
        # Display goodbye message and exit program by breaking while loop
        print("\nExiting Money Manager... See you again!")
        break
    else:
        # Display error message if choice is not within options
        print("\nInvalid choice! Please enter a valid option (1 - 6).")

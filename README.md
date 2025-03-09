# Money Manager - Income/Expense Tracker

## Overview
Welcome to the **Money Manager**, a simple and user-friendly program designed to help you manage your income and expenses. This program allows you to add transactions, view your transaction history, calculate total income and expenses, and save or load your transactions to/from a file. Whether you're tracking your monthly budget or keeping an eye on your finances, this tool has got you covered!

---

## Features
1. **Add Transactions**: Add income or expense transactions with a specified amount.
2. **View Transactions**: Display all your transactions in a clear and organized format.
3. **Calculate Totals**: Calculate and display your total income, total expenses, and net total (income - expenses).
4. **Load Transactions**: Load your saved transactions from a file (`transactions.txt`).
5. **Save Transactions**: Save your transactions to a file, with the option to either **add** to the existing file or **overwrite** it.
6. **Exit**: Exit the program gracefully.

---

## How to Use
1. **Run the Program**: Execute the program to start the Money Manager.
2. **Choose an Option**: You will be presented with a menu of options:
   - **1**: Add a new transaction (income or expense).
   - **2**: View all your transactions.
   - **3**: Calculate and display your total income, expenses, and net total.
   - **4**: Load transactions from the `transactions.txt` file.
   - **5**: Save your transactions to the `transactions.txt` file.
   - **6**: Exit the program.
3. **Follow Prompts**: Depending on your choice, the program will guide you through the process with clear prompts.
4. **Error Handling**: If you enter invalid input, the program will display an error message and allow you to try again.

---

## File Handling
- **Save Transactions**: When saving transactions, you can choose to either:
  - **Add** to the existing file (appends new transactions to the file).
  - **Overwrite** the file (replaces the file content with the current transactions).
- **Load Transactions**: Transactions are loaded from the `transactions.txt` file. Ensure the file exists and is formatted correctly.

---

## Example Usage
### Adding a Transaction
1. Choose option **1**.
2. Enter the transaction type (`Income` or `Expense`).
3. Enter the transaction amount (e.g., `100.50`).

### Viewing Transactions
1. Choose option **2**.
2. The program will display all transactions in the format:
   ```
   Type: Income    Amount: $100.50
   Type: Expense   Amount: $50.00
   ```

### Calculating Totals
1. Choose option **3**.
2. The program will display:
   ```
   Total Income: $100.50
   Total Expense: $50.00
   Net Total: $50.50
   ```

### Saving Transactions
1. Choose option **5**.
2. Select whether to **add** to the file or **overwrite** it.
3. Transactions will be saved to `transactions.txt`.

### Loading Transactions
1. Choose option **4**.
2. Transactions will be loaded from `transactions.txt`.

---

## Requirements
- Python 3.x
- A text file named `transactions.txt` (will be created automatically if it doesn't exist).

---

## Notes
- The program is designed to handle invalid inputs gracefully, ensuring a smooth user experience.
- Transactions are stored in a list of dictionaries, with each transaction having a `Type` (Income/Expense) and an `Amount`.
- The `transactions.txt` file is used for persistent storage of transactions.

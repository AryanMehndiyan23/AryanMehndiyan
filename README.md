# Campus Expense Tracker

## 1. Project Overview

Campus Expense Tracker is a basic Python program for recording and analyzing student campus expenses.

The program allows the user to add expenses with an expense name, category and amount. It can display all recorded expenses, calculate total spending, show category-wise spending and find the category with the highest spending.

## 2. Features

- Add Expense
- View Expenses
- Calculate Total Spending
- Show Category-wise Spending
- Find Highest Spending Category
- Simple menu-based interface
- Displays a message when no expenses are available
- Handles invalid menu choices

## 3. Technologies / Tools Used

- **Programming Language:** Python 3
- **Editor:** VS Code or any Python-supported editor
- **Version Control:** Git and GitHub
- **Libraries:** No external libraries are required.

## 4. Steps to Install & Run the Project

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Open the Project

Open the Campus Expense Tracker project folder in VS Code or a terminal.

### Step 3: Check the Project Files

Make sure the project contains:

```text
Campus_Expense_Tracker/
│
├── main.py
├── README.md
└── statement.md
```

### Step 4: Run the Program

Open the terminal in the project folder and run:

```bash
python main.py
```

If `python` does not work, try:

```bash
python3 main.py
```

## 5. Instructions for Testing

Test the program by using each menu option and checking the displayed result.

### Test 1: Add Expense

1. Run the program.
2. Select option `1`.
3. Enter an expense name, category and amount.
4. Check that **Expense added successfully** is displayed.

### Test 2: View Expenses

1. Select option `2`.
2. Check that the recorded expenses are displayed.

### Test 3: Total Spending

1. Add one or more expenses.
2. Select option `3`.
3. Check that the total amount of all expenses is displayed.

### Test 4: Category-wise Spending

1. Add expenses from different categories.
2. Select option `4`.
3. Check that the spending for each category is displayed.

### Test 5: Highest Spending Category

1. Add expenses in different categories.
2. Select option `5`.
3. Check that the category with the highest spending and its amount are displayed.

### Test 6: No Expenses

1. Start the program without adding an expense.
2. Select options such as View Expenses, Category-wise Spending or Highest Spending Category.
3. Check that **No expenses found** is displayed.

### Test 7: Invalid Choice

1. Enter a menu option other than `1` to `6`.
2. Check that **Invalid choice** is displayed.

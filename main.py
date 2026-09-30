print("===== CAMPUS EXPENSE TRACKER =====")

expenses = []
categories = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Show Category-wise Spending")
    print("5. Show Highest Spending Category")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter expense name: ")
        category = input("Enter category (food/travel/stationery): ")
        amount = float(input("Enter amount: "))

        expenses.append([title, category, amount])

        if category not in categories:
            categories.append(category)

        print("Expense added successfully.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\n===== ALL EXPENSES =====")
            for expense in expenses:
                print("Name:", expense[0],
                      "| Category:", expense[1],
                      "| Amount: ₹", expense[2])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[2]

        print("Total spending: ₹", total)

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\n===== CATEGORY-WISE SPENDING =====")

            for category in categories:
                category_total = 0

                for expense in expenses:
                    if expense[1] == category:
                        category_total = category_total + expense[2]

                print(category, ": ₹", category_total)

    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            highest_category = ""
            highest_amount = 0

            for category in categories:
                category_total = 0

                for expense in expenses:
                    if expense[1] == category:
                        category_total = category_total + expense[2]

                if category_total > highest_amount:
                    highest_amount = category_total
                    highest_category = category

            print("Highest spending category:", highest_category)
            print("Amount spent: ₹", highest_amount)

    elif choice == "6":
        print("Thank you for using Campus Expense Tracker.")
        break

    else:
        print("Invalid choice.")

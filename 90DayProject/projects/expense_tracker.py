import csv


def load_expenses(filename):
    expenses = []
    with open(filename,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            row['amount'] =  float(row['amount'])
            expenses.append(row)
    return expenses


expenses = load_expenses('projects/expenses.csv')
#print(expenses)


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)

def calculate_average(expenses):
    return calculate_total(expenses)/ len(expenses) if expenses else 0

def find_largest_expense(expenses):
    if not expenses:
        return None
    return max(expenses , key=lambda x: x["amount"])

def find_smallest_expense(expenses):
    if not expenses:
        return None
    return min(expenses, key=lambda x: x["amount"])


def calculate_category_total(expenses,category):
    return sum(expense["amount"] for expense in expenses if expense["category"] == category)

def category_summary(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += expense["amount"]

    return category_totals



def add_expense(expenses, category, amount, description):
    new_expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(new_expense)

    return expenses



def save_expenses(filename, expenses):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)



add_expense(expenses, "Food", 45, "Dinner")
save_expenses("projects/expenses.csv", expenses)



print("Loading expenses...")
print("Total expense: ", calculate_total(expenses))
print("Average expense: ", calculate_average(expenses))
print("Largest expense: ", find_largest_expense(expenses))
print("Smallest expense: ", find_smallest_expense(expenses))
print('Drinks expenses: ', calculate_category_total(expenses,"Drinks"))


category_totals = category_summary(expenses)
print("Category Summary:")
for category, total in category_totals.items():
    print(f'{category}: {total}')



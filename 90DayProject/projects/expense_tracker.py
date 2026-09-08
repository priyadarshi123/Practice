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

def add_expense(category, amount, description):
    new_expense = {
        "category": category,
        "amount": amount,
        "description": description}

    expenses.append(new_expense)


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)

def calculate_average(expenses):
    return calculate_total(expenses)/ len(expenses) if expenses else 0


print('Total expenses: ', calculate_total(expenses))

print('Average expenses: ', calculate_average(expenses))

def calculate_category_total(category):
    return sum(expense["amount"] for expense in expenses if expense["category"] == category)

def category_summary(expense):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += expense["amount"]
    return category_totals


print('Category Summary:')
for category, total in category_summary(expenses).items():
    print(f'{category}: {total}')

    
print('Drinks expenses: ', calculate_category_total("Drinks"))


expenses = [
    {
        "category": "Food",
        "amount": 25,
        "description": "Lunch"
    },
    {
        "category": "Transport",
        "amount": 15,
        "description": "Taxi"
    },
    {
        "category": "Tickets",
        "amount": 30,
        "description": "party"
    },
    {
        "category": "Fun",
        "amount": 130,
        "description": "Fun"
    },
    {
        "category": "Drinks",
        "amount": 90,
        "description": "Drinks"
    }
]


total = sum(expense["amount"] for expense in expenses)

print("Total expenses:", total)

average = total / len(expenses) if expenses else 0

print("Average expenses:", average)

largest_expense = max(expenses, key=lambda x: x["amount"]) if expenses else 0

print("Largest expense:", largest_expense)

smallest_expense = min(expenses, key=lambda x: x["amount"]) if expenses else 0

print("Smallest expense:", smallest_expense)

food_spending = sum(expense["amount"] for expense in expenses if expense["category"] == "Food")

print("Food expense:", food_spending)

transport_spending = sum(expense["amount"] for expense in expenses if expense["category"] == "Transport")

print("Transport expense:", transport_spending)


def add_expense(category, amount, description):
    new_expense = {
        "category": category,
        "amount": amount,
        "description": description}

    expenses.append(new_expense)


def calculate_total():
    return sum(expense["amount"] for expense in expenses)

def calculate_average():
    return calculate_total()/ len(expenses) if expenses else 0


print(calculate_total())

print(calculate_average())


import matplotlib.pyplot as plt

import pandas as pd


df = pd.read_csv("90dayProject/projects/cleaned_expenses.csv")
print(df)

category_expenses = df.groupby("category")["amount"].sum()

print(category_expenses)

category_expenses.plot(kind = "bar")

plt.title("Spending by category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.savefig("90dayProject/projects/spending_by_category.png")
plt.show()

plt.figure()

df["amount"].plot(kind="hist", bins=5)

plt.title("Distribution of expenses")
plt.xlabel("Expense amount")
plt.ylabel("Number of transactions")

plt.tight_layout()
plt.savefig("90dayProject/projects/expense_distribution.png")

plt.show()


top_expenses = df.sort_values("amount", ascending=False).head(5)

top_expenses.plot(
    x="description",
    y="amount",
    kind="bar"
)

plt.title("top expenses")
plt.xlabel("category")
plt.ylabel("amount")
plt.tight_layout()
plt.savefig("90dayProject/projects/top_expenses.png")
plt.show()


category_percentage = category_expenses / df["amount"].sum() * 100

print(category_percentage)
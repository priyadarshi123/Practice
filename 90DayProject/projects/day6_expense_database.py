import pandas as  pd

df = pd.read_csv("90dayProject/projects/cleaned_expenses.csv")

print(df)

from pathlib import Path
import sqlite3


connection = sqlite3.connect("90dayProject/projects/expenses.db")

cursor = connection.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    description TEXT
)
""")

connection.commit()

for index,row in df.iterrows():

    cursor.execute("""
    SELECT 1
    FROM expenses
    WHERE category = ?
      AND amount = ?
      AND description = ?
""", (row['category'], row['amount'], row['description']))

    existing = cursor.fetchone()

    if existing:
        print("Already exists - skipping")
    else:

        cursor.execute("""
        INSERT INTO expenses (category, amount, description)
        VALUES (?, ?, ?)
        """, (row['category'], row['amount'], row['description']))

    connection.commit()



cursor.execute("SELECT * FROM expenses")

rows = cursor.fetchall()

print("All expenses")
for row in rows:
    print(row)


cursor.execute("SELECT  category, amount FROM expenses")

rows = cursor.fetchall()

print(" Category and Amount")

for row in rows:
    print(row)


cursor.execute("SELECT * FROM expenses where amount > 50")

rows = cursor.fetchall()

print("Expenses greater than 50")

for row in rows:
    print(row)


cursor.execute("SELECT * FROM expenses where amount = (select max(amount) from expenses)")

rows = cursor.fetchall()

print("Max expense")

for row in rows:
    print(row)



cursor.execute("SELECT Sum(amount) FROM expenses")

rows = cursor.fetchall()

print("Total spending")

for row in rows:
    print(row)



cursor.execute("SELECT Avg(amount) FROM expenses")

rows = cursor.fetchall()

print("Average spending")

for row in rows:
    print(row)



cursor.execute("SELECT category, avg(amount) FROM expenses group by category")

rows = cursor.fetchall()

print("Average spending by category")

for row in rows:
    print(row)



cursor.execute("SELECT category,sum(amount) FROM expenses group by category")

rows = cursor.fetchall()

print("Total spending by category")

for row in rows:
    print(row)




cursor.execute("SELECT min(amount) FROM expenses")

rows = cursor.fetchall()

print("Minimum  expense")

for row in rows:
    print(row)




cursor.execute("SELECT *  FROM expenses order by amount desc limit 3 ")

rows = cursor.fetchall()

print("Top 3 expense")

for row in rows:
    print(row)

connection.close()



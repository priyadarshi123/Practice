from pathlib import Path
import sqlite3

connection = sqlite3.connect("Practice/90dayProject/projects/expenses.db")

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


cursor.execute("""
INSERT INTO expenses (category, amount, description)
VALUES (?, ?, ?)
""", ("travel", 40, "temple"))

connection.commit()

cursor.execute("SELECT * FROM expenses")

rows = cursor.fetchall()

print("All expenses")
for row in rows:
    print(row)


cursor.execute("SELECT DISTINCT category, amount FROM expenses")

rows = cursor.fetchall()

print("Unique Category and Amount")

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

connection.close()


import pandas as  pd

df = pd.read_csv("90dayProject/projects/messy_expenses.csv")

#print(df.info())

print("Rows before cleaning:", len(df))

print("Missing values before cleaning:")
print(df.isna().sum())

print("Duplicate rows before cleaning:", df.duplicated().sum())

      

df['amount'] = df['amount'].str.replace('$','')

df = df.dropna(subset=["amount"])

df['amount'] = pd.to_numeric(df['amount'])

df['category'] = df['category'].str.strip().str.lower()

df = df.drop_duplicates()

print("Rows after cleaning:", len(df))

print("Missing values after cleaning:")
print(df.isna().sum())

print("Duplicate rows after cleaning:", df.duplicated().sum())


print("Total spending:", df["amount"].sum())
print("Average spending:", df["amount"].mean())
print(df.groupby("category")["amount"].sum())
print(df[df["amount"] > 100])
print(df[(df["category"] == "food") & (df["amount"] > 20)])


df.to_csv("90dayProject/projects/cleaned_expenses.csv", index=False)

'''

#print(df.describe())

#food = df[df['category'] == 'Food']

#print(food['amount'])

#print(df[df['category'] == 'Food']['amount'].sum())

#print(df.sort_values('amount',ascending=False))

#print(df.groupby('category')['amount'].mean())



print('Number of Transactions:',df.shape[0])

print('Number of unique categories:', len(df['category'].unique()))

print('Total spending:', df['amount'].sum())

print('Mean spending:', df['amount'].mean())

print('Minimum expense:', df['amount'].min())

print('Maximum expense:', df['amount'].max())

print('Spending by category:')

print(df.groupby('category')['amount'].sum())

# Top 3 expenses
print(df.sort_values('amount',ascending = False).head(3))

# Top 3 categories with greatest expenses
print(df.groupby('category')['amount'].sum().sort_values(ascending = False).head(3))
'''





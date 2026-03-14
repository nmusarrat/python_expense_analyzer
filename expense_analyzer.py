import pandas as pd
import matplotlib.pyplot as plt

#load csv
data=pd.read_csv('expenses.csv',header=None)

#name columns
data.columns=['Date','Item','Amount']

print('First 5 rows of the data:')
print(data.head())

#total spending
total=data['Amount'].sum()
print('\nTotal spent:',total)

#avarage expenses
ave=data['Amount'].mean()
print('\nAverage expense:',ave)

#largest expense
largest=data['Amount'].max()
print('\nLargest expense:',largest)

#expenses by category
category_total=data.groupby('Item')['Amount'].sum()
print('\nSpending by category:')
print(category_total)

#sort expenses
sorted_expenses=data.sort_values('Amount',ascending=False)
print('\nTop expenses:')
print(sorted_expenses.head())

#create a bar chart
category_total.plot(kind='pie',autopct='%1.1f%%')
#add titles
plt.title('Expense by category')
#display chart
plt.show()

print('\nTop 3 biggest expenses:')
top3=data.sort_values('Amount',ascending=False).head(3)
print(top3)


#export report
category_total.to_excel('expense_summary.xlsx')
print('\nExcel report created:expense_summary.xlsx')

#show common expenses
print('\nMost common expense categories:')
print(data['Item'].value_counts())


#category with the highest spending
top_category=category_total.idxmax()
print('\nYou spent the most money on:',top_category)
max_amount=category_total.max()
print('Total spent on it:',max_amount)

#statistic summary
print('\nstatistics summary:')
print(data['Amount'].describe())

#dataset structure
print('\nDataset information:')
print(data.info())







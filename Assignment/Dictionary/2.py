# 2.Write a Python program to combine values in python list of dictionaries
from collections import Counter
listof_dict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for i in listof_dict:
    result[i['item']] += i['amount']
print(result)

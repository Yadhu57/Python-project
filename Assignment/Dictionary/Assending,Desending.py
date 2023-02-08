dict1 = {5: 2, 6: 4, 9: 3, 8: 1, 7: 0}
print("Dictionary:", dict1)


sort_data = sorted(dict1.items())
sort_data_dict = dict(sort_data)
print("Ascending:", sort_data_dict)


sort_data = sorted(dict1.items(), reverse=True)
sort_data_dict2 = dict(sort_data)
print("Descending:", sort_data_dict2)

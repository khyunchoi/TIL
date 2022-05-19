dictionary = {'spy': 3, 'ray': 2, 'room': 1, 'once': 2}
sorted_dict = sorted(dictionary.items(), key=lambda x:(-x[1],x[0]))

print(sorted_dict)
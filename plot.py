import csv
import matplotlib.pyplot as plt
import numpy as np

data_json = {}

with open('raw.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\tIn {row["Year"]} there are {row["Live Births"]} {row["Race"]} were born.')
        race = row["Race"].split(" ")[0]
        births = int(row["Live Births"])
        if race == 'All' or race == 'American':
            continue
        if data_json.get(row["Race"]) is None:
            data_json[race] = births
        else:
            data_json[race] += births
        line_count += 1
    print(f'Processed {line_count} lines.')

print(data_json.keys())
print(data_json.values())

x = np.array(list(data_json.keys()))
y = np.array(list(data_json.values()))

plt.bar(x,y)
plt.show()

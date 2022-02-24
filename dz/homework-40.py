import requests
import json
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3850', 'London, Best str']
        ]
#
with open('data2.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(data)

with open('data2.csv') as f:
    print(f.read())

with open('data2.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(data)

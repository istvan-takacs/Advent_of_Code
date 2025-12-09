import csv
import re

invalid_ids = []
pattern = re.compile(r"^(.*)\1+$")

with open('day2_input.md', 'r') as f:
    csv_file = csv.reader(f)
    data = list(csv_file)[0]

for id_range in data:
    split_range = re.split("-",id_range)
    start_of_range = int(split_range[0])
    end_of_range = int(split_range[1])

    for id in range(start_of_range, end_of_range + 1):
        
        repeat = re.findall(pattern, str(id))
        if repeat:
            invalid_ids.append(id)

# print(invalid_ids)
print(sum(invalid_ids))


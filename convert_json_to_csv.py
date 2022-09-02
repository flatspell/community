import json
import csv

json_filepath = "ntee.json"
csv_filepath = "ntee.csv"

with open(json_filepath, 'w') as filename:
        json.dump(page, filename)

        # df = pd.read_json(filename)
        # print(page)
        # print(df.head())

with open(json_filepath) as json_file:
    data = json.load(json_file)
    
# now we will open a file for writing
data_file = open(csv_filepath, 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for org in organization_data:
    if count == 0:

        # Writing headers of CSV file
        header = org.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(org.values())

data_file.close()
import requests
import json
import csv
import pandas as pd

project_dir = "/Users/lucaswiley/Desktop/nonprofits"
json_dir = project_dir + "/json/"
csv_dir = project_dir + "/csv/"

session = requests.Session()

def get_wa_responses():
    url = "https://projects.propublica.org/nonprofits/api/v2/search.json?state%5Bid%5D=WA" 
    first_page = session.get(url).json()
    # yield first_page
    num_pages = first_page['num_pages']

    for page_number in range(96, num_pages + 1):
      next_page = session.get(url, params={'page': page_number}).json()
      yield next_page

page_number = 96
# while page_number < 5:
for page in get_wa_responses():
    json_filepath = json_dir + 'test_data_file_{page}.json'.format(page=page_number)
    csv_filepath = csv_dir + 'test_data_file_{page}.csv'.format(page=page_number)

    with open(json_filepath, 'w') as filename:
        json.dump(page, filename)

        # df = pd.read_json(filename)
        # print(page)
        # print(df.head())

    with open(json_filepath) as json_file:
        data = json.load(json_file)
    
        organization_data = data["organizations"]
        organization_name = organization_data[0]["name"]
        organization_city = organization_data[0]["city"]
        
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

    print ("Incrementing page " + str(page_number) + " starting with organization: " + str(organization_name) + " in " + str(organization_city))
    page_number += 1

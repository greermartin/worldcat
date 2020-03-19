import csv
import json
import requests

# worldcat library locations lookup by oclc number resource URL
host = 'http://www.worldcat.org/webservices/catalog/content/libraries/'

# get auth key
local_file = 'worldcat_auth.txt' 
with open(local_file) as txtfile: 
    my_key = txtfile.read() 
     #  print("API Key: " + my_key)

# get all libraries in US for oclc number, count the libraries       
def get_libraries(oclc, api_key):    
    url = host + oclc + "?wskey=" + api_key + "&location=illinois&maximumLibraries=100&format=json" # form URL
    response = requests.request('GET', url) # make request
    libraries = response.json() # return all libraries
    return(len(libraries['library'])) # count libraries by counting json objects   

# open and read csv containig oclc numbers
csvfile = open("batch.csv", 'r')
header = csvfile.readline()
csvfile.close()

# print(header) # a string with newline and commas
header = header.strip('\n') # remove the new line character
fieldnames = header.split(',') 

# prepare output csv
with open("batch.csv", "r") as infile, \
    open("batch_count_il.csv", "w") as outfile:
        
# create a reader object to read rows from your infile
    reader = csv.DictReader(infile, fieldnames)
    next(reader, None) # skip over the header row   

# create a writer object to add rows to your outfile
    fieldnames.append('IL_COUNT') # name for new column
    writer = csv.DictWriter(outfile, fieldnames)
    writer.writeheader()
    
# get oclc number from infile, add library count, save all to outfile
    for title in reader:
        oclcNo = title['OCLC Number']
        printLibraries = get_libraries(oclcNo, my_key)
        title['IL_COUNT'] = printLibraries
        writer.writerow(title)

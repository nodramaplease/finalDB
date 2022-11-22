import csv
import json
from pymongo import MongoClient
import urllib.parse
import time
import datetime


# Create connection to MongoDB
username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('password')
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
db = client['test']
collection = db['cinemas']

csvFilePath = r'cinema.csv'
logs = []

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, logsList):	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			data = {}
			name = rows['name']
			city = rows['city']
			opening = rows['opening']
			closing = rows['closing']
			halls_count=rows['halls_count']
			avg_ticket_price=rows['avg_ticket_price']
			movies_count=rows['movies_count']
			tp = rows['type']
			customers_count = rows['customers_count']

			data["name"] = name
			data["city"] = city
			data["opening"] = datetime.datetime.strptime(opening, "%H:%M:%S%z")
			# print(datetime.datetime.strptime(opening, "%H:%M:%S%z").timetz())
			data["closing"] = datetime.datetime.strptime(closing, "%H:%M:%S%z")
			data["halls_count"] = int(halls_count)
			data["avg_ticket_price"] = float(avg_ticket_price)
			data["movies_count"] = int(movies_count)
			data["type"] = tp
			data["customers_count"]=int(customers_count)
			logsList.append(data)
		



make_json(csvFilePath, logs)
print(logs)

for log in logs:
	# Insert the dictionary into Mongo
	collection.insert_one(log)

#!/usr/bin/python
import datetime
from influxdb import InfluxDBClient
from datetime import datetime
from influxdb.line_protocol import _get_unicode, quote_ident, _is_float, text_type
import urllib3
import json


# Define URL
url = 'http://domail.tld/json-url'

# Create PoolManager
http = urllib3.PoolManager()

# Sending a GET request and getting back response as HTTPResponse object.
resp = http.request("GET", url)

# Convert string to Python json
json_str = json.loads(resp.data.decode('utf-8'))

# Create dime format readable for influx
current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

# Change sring into float
# I experienced influx did not read the keys as number. So i make a small loop in order to change the type in this specific case to fload.
for key in json_str:
    json_str[key] = float(json_str[key])

# Build a body compatible with influxdb
json_body = [
    {
        "measurement": "Some measurement name",
        "time": current_time,
        "fields": json_str
    }
]

# Connect to influxdb 
# you can add username and passwords to this line aswell 
# client = InfluxDBClient(host, port, user, password, dbname)
client = InfluxDBClient(host='localhost', port=8086)

# Selecte database in influx client (change databasename to the name of the database you like to fill with your data)
client.switch_database('databasename')

# Write to influxdb
client.write_points(json_body)


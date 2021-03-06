
import sys
import http.client
import json


city_request = input("Select the city of which you want to know the weather: ")
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query=" + city_request
print(ENDPOINT)
METHOD = "GET"
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
print()
print("Response received: ", end='')
print(r1.status, r1.reason)
input_response = r1.read().decode("utf-8")
conn.close()
metainfo = json.loads(input_response)
if len(metainfo)==0:
    print("Sorry the city that you have introduced does not exist in our data base")
    sys.exit(0)



woeid = metainfo[0]["woeid"]






# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"


LOCATION_WOEID = str(woeid)
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
weather = json.loads(text_json)

# -- Get the data
time = weather['time']
sun_set = weather["sun_set"]

temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']


print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))
print("Time of sunset: {} ".format(sun_set))

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing


# -- Generate the object from the json file
joke = json.loads(text_json)
joke_chuck=(joke["value"]["joke"])
print("A random joke of Chuck Norris is: ", joke_chuck)
print(" ")


ENDPOINT = "/jokes/count"

conn = http.client.HTTPConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
response = json.loads(text_json)

number_of_jokes = response["value"]
print("The number of jokes are:", number_of_jokes)


ENDPOINT = "/categories"

conn = http.client.HTTPConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
response = json.loads(text_json)

number_of_categories = len(response["value"])
print("The number of categories:", number_of_categories)
print("The categories are: ")
for n in response["value"]:
    print("     ", n)


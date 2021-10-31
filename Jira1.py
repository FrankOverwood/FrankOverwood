

import base64
cred =  "Basic " + base64.b64encode(b'ahmadnm@gmail.com:QVlGxjuBgvdG1VOUB6La348E').decode("utf-8")
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": cred
}


import requests
import json
import base64

# Base encode email and api token
cred =  "Basic " + base64.b64encode(b'ahmadnm@gmail.com:QVlGxjuBgvdG1VOUB6La348E').decode("utf-8") 
# Set header parameters
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization" : cred
}

# Enter your project key here
projectKey = "PKY"

# Update your site url 
url = "https://datanest101.atlassian.net/rest/api/3/search?jql=project=" + projectKey

# Send request and get response
response = requests.request(
   "GET", 
   url,
   headers=headers
)

# Decode Json string to Python
json_data = json.loads(response.text)

# Display issues
for item in json_data["issues"]:
    print(item["id"] + "\t" + item["key"] + "\t" +
        item["fields"]["issuetype"]["name"] + "\t" +
        item["fields"]["created"]+ "\t" +
        item["fields"]["creator"]["displayName"] + "\t" +
        item["fields"]["status"]["name"] + "\t" +
        item["fields"]["summary"] + "\t" 
        )



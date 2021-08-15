import json
import urllib.request

url = "your_url_here"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data)
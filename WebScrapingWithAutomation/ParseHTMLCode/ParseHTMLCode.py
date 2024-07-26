import requests
from bs4 import BeautifulSoup

# Define the url
url = "https://www.rottentomatoes.com"

# Send a request to get html code from that url
response = requests.get(url, headers={"Accept": "text/html"})

# Parse the response
parsed_response = BeautifulSoup(response.text, "html.parser")

# Format the parsed HTML response in a way that’s easier to read and print it out
print(parsed_response.prettify())

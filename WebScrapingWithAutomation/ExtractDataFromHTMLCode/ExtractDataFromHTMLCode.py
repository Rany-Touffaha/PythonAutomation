import requests
from bs4 import BeautifulSoup

# Define the url
url = "https://www.rottentomatoes.com"

# Send a request to get html code from that url
response = requests.get(url, headers={"Accept": "text/html"})

# Parse the response
parsed_response = BeautifulSoup(response.text, "html.parser")

# Find all movie titles
titles = parsed_response.findAll("span", class_="p--small")

# Iterate over the titles and print the text for each
for title in titles:
    print(title.text)


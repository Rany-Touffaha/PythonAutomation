import requests
from bs4 import BeautifulSoup
from time import sleep

# for loop to iterate over the range of page numbers you want to scrape from
for page_number in range(1, 4):
    # define the url
    url = "https://www.playstationtrophies.org/archive/gaming-news/" + str(page_number) + "/"

    # send a request to get html code from that url
    response = requests.get(url, headers={"Accept": "text/html"})

    # parse the response
    parsed_response = BeautifulSoup(response.text, "html.parser")

    # extract all the headlines specific to news titles from that page
    headline_elements = parsed_response.find_all("h4", class_="h-5")

    # extract all the decks specific to news titles from that page
    deck_elements = parsed_response.find_all("p", class_="list__descr")

    # print out the page number
    print("\nPage Number:", page_number)

    # print out the headlines
    print("\nNews Headlines:", list(map(lambda x: x.text.strip(), headline_elements)))

    # print out the decks
    print("\nNews Decks:", list(map(lambda x: x.text.strip(), deck_elements)))

    # pause the program for 1 second between iterations of the loop
    sleep(1)

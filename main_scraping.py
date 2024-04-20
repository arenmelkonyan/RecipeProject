import requests
from bs4 import BeautifulSoup


def getting_links():
    url = "https://www.foodnetwork.com/recipes"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    links = soup.findAll("h3", class_="m-MediaBlock__a-Headline")[6:15]
    for link in links:
        link_url = link.find("a")['href']
        if link_url.startswith('//'):
            link_url = 'https:' + link_url
        yield link_url


def scrape_recipe(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    ingredients = soup.findAll("span", class_="o-Ingredients__a-Ingredient--CheckboxLabel")[1:15]
    for ingredient in ingredients:
        yield ingredient.text


def getting_links_and_recipes():
    for link_url in getting_links():
        print("URL:", link_url)
        for ingredient in scrape_recipe(link_url):
            print("Ingredient:", ingredient)


getting_links_and_recipes()

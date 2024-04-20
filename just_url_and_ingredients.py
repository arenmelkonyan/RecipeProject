import requests
from bs4 import BeautifulSoup

url = "https://www.foodnetwork.com/recipes"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")


def getting_links():
    # global link_url
    links = soup.findAll("h3", class_="m-MediaBlock__a-Headline")[6:15]
    for link in links:
        link_url = link.find("a")['href']
        if link_url.startswith('//'):
            link_url = 'https:' + link_url
        yield link_url


def getting_recipes():
    recipes = soup.findAll("span", class_="m-MediaBlock__a-HeadlineText")[7:16]
    for recipe in recipes:
        name = recipe.text
        print(name)


# getting_links()
def scraping_recipe(link_url):
    response = requests.get(link_url)
    soup = BeautifulSoup(response.content, 'lxml')
    Ingredients = soup.findAll("span", class_="o-Ingredients__a-Ingredient--CheckboxLabel")[1:15]
    for Ingredient in Ingredients:
        Ingredient_list = Ingredient.text
        yield Ingredient_list


def getting_links_and_recipes():
    for link_url in getting_links():
        print(f"URL: {link_url}")
        for ingredient in scraping_recipe(link_url):
            print(f"Ingredients: {ingredient}")


getting_links_and_recipes()

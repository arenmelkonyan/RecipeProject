from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup

engine = create_engine("sqlite:///recipes.db", echo=True)
Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    URL = Column(String)
    ingredients = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

url = "https://www.foodnetwork.com/recipes"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")


def getting_links():
    links = soup.findAll("h3", class_="m-MediaBlock__a-Headline")[6:15]
    for link in links:
        link_url = link.find("a")['href']
        if link_url.startswith('//'):
            link_url = 'https:' + link_url
        yield link_url, link.text.strip()


def scraping_recipe(link_url):
    response = requests.get(link_url)
    soup = BeautifulSoup(response.content, 'lxml')
    ingredients = soup.findAll("span", class_="o-Ingredients__a-Ingredient--CheckboxLabel")[1:15]
    ingredient_list = ", ".join([ingredient.text for ingredient in ingredients])
    return ingredient_list


def getting_links_and_recipes():
    for link_url, name in getting_links():
        print(f"URL: {link_url}")
        ingredients = scraping_recipe(link_url)
        print(f"Ingredients: {ingredients}")
        recipe = Recipe(name=name, URL=link_url, ingredients=ingredients)
        session.add(recipe)
        session.commit()


getting_links_and_recipes()

import unittest
from unittest.mock import patch, MagicMock
from recipes import getting_links, scraping_recipe


class TestRecipeScraping(unittest.TestCase):

    @patch('recipes.py')
    def test_getting_links(self, mock_get):
        mock_response = MagicMock()
        mock_response.content = """
            <html>
            <body>
            <h3 class="m-MediaBlock__a-Headline"><a href="//www.example.com">Recipe 1</a></h3>
            <h3 class="m-MediaBlock__a-Headline"><a href="//www.example.com">Recipe 2</a></h3>
            </body>
            </html>
        """
        mock_get.return_value = mock_response

        links = list(getting_links())

        self.assertEqual(len(links), 9)
        self.assertEqual(links[0][0], "https://www.example.com")
        self.assertEqual(links[0][1], "Recipe 1")
        self.assertEqual(links[1][0], "https://www.example.com")
        self.assertEqual(links[1][1], "Recipe 2")

    @patch('recipes.requests.get')
    def test_scraping_recipe(self, mock_get):
        mock_response = MagicMock()
        mock_response.content = """
            <html>
            <body>
            <span class="o-Ingredients__a-Ingredient--CheckboxLabel">Ingredient 1</span>
            <span class="o-Ingredients__a-Ingredient--CheckboxLabel">Ingredient 2</span>
            </body>
            </html>
        """
        mock_get.return_value = mock_response

        ingredients = scraping_recipe("https://www.foodnetwork.com/recipes")

        self.assertEqual(ingredients, "Ingredient 1, Ingredient 2")


if __name__ == '__main__':
    unittest.main()

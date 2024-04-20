class Basemodelclass:
    def __init__(self, id):
        self.id = id


class Recipe(Basemodelclass):
    def __init__(self, id, name, ingredients, preparation, instructions):
        super().__init__(id)
        self.preparation = preparation
        self.id = id
        # self.category = category
        self.name = name
        self.ingredients = ingredients
        # self.preparation = preparation
        self.instructions = instructions

    def display_recipe_info(self):
        print(f"ID: {self.id}")
        # print(f"Category: {self.category}")
        print(f"Name: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Preparation: {self.preparation}")
        print(f"Step-by-step directions: {self.instructions}")


recipes = Recipe(4, "Borsh", "Bazuk kaxamb...", "kastrulken dnum eq gazin...", "senc senc senc")
# recipes.add_tag("Vegetarian")
recipes.display_recipe_info()


class User(Basemodelclass):
    def __init__(self, id, name, email, password):
        super().__init__(id)
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def display_user_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        # print(f"Password: {self.password}")


class Category(Basemodelclass):
    def __init__(self, id, name, tags=None):
        super().__init__(id)
        self.name = name
        self.tags = tags if tags else []

    def add_tag(self, tag):
        self.tags.append(tag)

    def display_category(self):
        print(f"Category name: {self.name}")
        print(f"Tag name: {self.tags}")


categories = Category(23, "Spas")
categories.add_tag("Vegetarian")
categories.display_category()

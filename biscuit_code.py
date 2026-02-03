class Biscuit:
    def __init__(self, name, ingredients, bake_time_minutes):
        self.name = name
        self.ingredients = ingredients
        self.bake_time_minutes = bake_time_minutes
    
    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Bake time: {self.bake_time_minutes} minutes")
    
    def scale_recipe(self, servings):
        print(f"\nScaling recipe for {servings} servings")
        scaled_time = self.bake_time_minutes
        print(f"Bake time remains: {scaled_time} minutes")


# Example usage
classic_biscuit = Biscuit(
    name="Classic Butter Biscuit",
    ingredients=["flour", "butter", "sugar", "eggs", "baking powder"],
    bake_time_minutes=12
)

classic_biscuit.display_recipe()
classic_biscuit.scale_recipe(2)
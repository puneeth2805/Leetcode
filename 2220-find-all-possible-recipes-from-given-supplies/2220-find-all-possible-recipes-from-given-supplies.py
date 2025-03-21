class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies=set(supplies)
        recipes=dict(zip(recipes,ingredients))
        recipe_made=[]
        while True:
            new_recipe=False
            for r,ing in [*recipes.items()]:
                if not all(i in supplies for i in ing):
                    continue
                recipe_made.append(r)
                supplies.add(r)
                del recipes[r]
                new_recipe=True
            if not new_recipe:
                break
        return recipe_made

        
        
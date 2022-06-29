# SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer
# database
from ..config.database import Base

# SQLAlchemy models

# Many-To-Many recipe/ingredient relationship
class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredient'

    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)


# Many-To-Many relationship:
    # I create an association table between RecipeInDB and IngredientInDB: RecipeIngredient
    # (later it'll have restrictions concerning creators' IDs when it's not a default ingredient)
    
    # Rows in RecipeInDB and IngredientInDB get created as normal
        # recipe = RecipeInDB(...)
        # ingredient1 = IngredientInDB(...)
        # db.session.add_all([recipe, ingredient1])
        # db.session.commit()
    
    # Then
        # recipe.ingredients.append(ingredient1)
        # db.session.commit()

    # to remove item:
        # recipe.ingredients.remove(ingredient1)
        # db.session.commit()

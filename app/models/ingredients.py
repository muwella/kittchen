# SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# database
from ..config.database import Base

# SQLAlchemy models

class IngredientInDB(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_default = Column(Boolean, default=True)
    creator_id = Column('creator', Integer, ForeignKey('users.id'), default=1)
    category_id = Column('category', Integer, ForeignKey('ingredient_categories.id'))


# WIP default ingredients
#   - fruits: [manzana roja, manzana verde, bananas, naranjas, mandanrinas, peras, frutillas,
#              sandía, cerezas, moras, frambuesas, arandanos, durazno, palta, coco, granada, kiwi,
#              limón, lima, mango, papaya, damasco, ananá, melón, maracuyá, higo, ciruela, membrillo,
#              pomelo, pomelo rosado, uvas verdes, uvas blancas, uvas negras]
#   - vegetables: [tomate, zanahoria, papa, batata, cebolla, cebolla de verdeo, coles de bruselas, apio,
#                  espinaca, acelga, ajo, lechuga, berenjena, pepino, chauchas, zapallo anco,
#                  zapallo cabutia, zapallito, morrón rojo, morrón amarillo, morrón verde, boñato,
#                  espárrago, champiñones, remolacha, colifor, brócoli, choclo, aceitunas, rúcula,
#                  radicheta]
#   - etc
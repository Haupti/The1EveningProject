
import Ingredient as I


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


kartoffelSpinatEi = Recipe("Kartoffeln mit Spinat und Ei", [I.rahmspinat, I.kartoffel, I.ei, I.salz, I.pfeffer])
kartoffelsalatBiGaStyle = Recipe("Kartoffelsalat BiGa Style", [I.kartoffel, I.zwiebelRot, I.guerkchen, I.essigHell, I.salz, I.pfeffer, I.oel, I.zucker])
        

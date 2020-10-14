class Ingredient:
    def __init__(self, name, portion, unit, location):
        self.name = name
        self.portionsGroesse = portion
        self.einheit = unit
        self.location = location

#Locations:
# og = obst und gemuese
# tk = tiefgefroren
# fem = fleisch, eier, milchprodukte und andere kuehlwahren
# ktb = kaffe, tee, backzutaten
# kfg = konserven, flaschen und gewuerze
# carb = carbs und so
# snk = snacks
# sonst = sonstiges

spaghetti = Ingredient("Spaghetti",75,"g","carb")
kartoffel = Ingredient("Kartoffel",250,"g","og")
ei        = Ingredient("Ei",1,"stk","fem")
rahmspinat= Ingredient("Rahmspinat",200,"g","tk")
zwiebelRot= Ingredient("Rote Zwiebel",0.5,"stk","og")
guerkchen = Ingredient("Guerkchen",5,"stk","kfg")
essigHell = Ingredient("Essig Hell",1,"EL","kfg")
salz      = Ingredient("Salz",1,"TL","kfg")
pfeffer   = Ingredient("Pfeffer",1,"TL","kfg")
oel       = Ingredient("Oel",1,"EL","kfg")
zucker    = Ingredient("Zucker", 1, "EL", "ktb")

import Recipe as R
import numpy as np
import config
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform

class Wochenplan:   
    def __init__(self, nummer, rezeptliste):
        self.number = nummer
        self.shoppingList = []
        self.recipeList = rezeptliste

    def makePrimaryShoppingList(self):
        primaryShoppingList = []
        for recipe in self.recipeList:
            for ingredient in recipe[0].ingredients:
                primaryShoppingList.append([ingredient, recipe[1]])

        return primaryShoppingList

    """
        This function takes the unordered, unsorted shoppinglist that contains
        doubles. It counts the portion amounts in total in the list of each
        ingredient and adds them up. It then writes them to a new list and returns
        the new list.

        Parameters:
        self - the class variables/methods

        Returns:
        shoppingList - shoppingList without double ingridients but with summed
                        portion numbers.
    """
    def makeFinalShoppingList(self):
        primaryShoppingList = self.makePrimaryShoppingList() 
        shoppingList = [] #new shopping list, that will be ordered without doubles
        """
            This is the actual logic:
                It runs throgh the unordered list, picks the first element
                looks how often it appears in the list and afterwards 
                deletes all occurences of this specific object from the 
                unordered list, and writes the object with the summed portions
                to the new list
        """
        while(len(primaryShoppingList)> 0):
            portions = 0 #portions total of the specific ingredient in the unordered list
            for element in primaryShoppingList: #runs throught the shoppinglist
                if element[0] == primaryShoppingList[0][0]: #if the current ingredient is the same as the first ingredient in the primary shopping list
                    portions += element[1] # then the number of portions is added to the variable defined above
            shoppingList.append([primaryShoppingList[0][0],portions]) #adds the element and the number of total portions to the new list
            primaryShoppingList = list(filter(lambda elem: elem[0] != shoppingList[-1][0], primaryShoppingList)) #filters out all elements that are unequal to the one currently searched and saves them to the primary shopping list, so we can iterate over it again in the next run of the while loop

        return shoppingList

    def sortedShoppingList(self):
       shoppingList = self.makeFinalShoppingList()
       shoppingList.sort(key= lambda elem: config.locationDict[elem[0].location])

       return shoppingList

    def printShoppingList(self):
        shoppingList = self.sortedShoppingList()
        for element in shoppingList:
            print(element[0].name + " : " + str(element[1]*element[0].portionsGroesse) + " " + str(element[0].einheit))

    def createPDFShoppingList(self):
        shoppingList = self.sortedShoppingList()

        c = canvas.Canvas('ShoppingList.pdf')

        form = c.acroForm

        for index,element in enumerate(shoppingList):
            entry = element[0].name + " : " + str(element[1]*element[0].portionsGroesse) + " " + str(element[0].einheit)
            c.drawString(50, 800 - index*40 , entry)
            form.checkbox(x=10, y= 800 - index*40, buttonStyle='check')

        c.save()


P0001 = Wochenplan(1, [[R.kartoffelSpinatEi, 7], [R.kartoffelsalatBiGaStyle,2]])

print(P0001.createPDFShoppingList())

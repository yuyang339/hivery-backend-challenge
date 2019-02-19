import json

with open('vegetable.json') as f:
    VEGITABLE = json.load(f)

with open('fruit.json') as f:
    FRUIT = json.load(f)

def isVegetable(food):
    return food in VEGITABLE

def isFruit(food):
    return food in FRUIT

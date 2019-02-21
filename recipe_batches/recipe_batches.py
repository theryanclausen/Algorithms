#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ing_keys = list(recipe)
  max_batch = {}
  for i in ing_keys:
    if not i in ingredients or recipe[i] > ingredients[i]:
      return 0
    max_batch[i] = ingredients[i] // recipe[i]

  return min(dict.values(max_batch))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
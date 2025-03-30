#! /bin/python3

from Crypto.Util.number import getPrime, bytes_to_long as btl, long_to_bytes as ltb
from random import shuffle
from math import prod
from secret import FLAG

assert FLAG.startswith("CodeVinciCTF{")
assert FLAG.endswith("}")

# Recipe for making chef CyberChef's world renouned "special soup"
# Add the ingredients to a pot full of boiling water
boiling_pot = ["onion", "pasta", "tomato", "pear", "fish oil", "tamarind", "basil", "courgette", "mince beef", "dynamite"]
boiling_pot.append(FLAG) # Add the secret ingredient
shuffle(boiling_pot) # Mix well all the ingredients
flavourless_dish = ", ".join(boiling_pot) # Pour the soup into a dish and proceed with adding more flavour to the soup

# Grab salt and pepper from the cupboard
salt = [getPrime(512) for _ in range(4)]
pepper = pow((1<<16)+1, -1, prod(s-1 for s in salt)) # I also mix my black pepper with salt to bring out the umami

# Add salt and pepper to your liking (I like to put in a ton of them)
tasty_dish = []
for i in range(4):
    salted_and_peppered = pow(pow(btl(flavourless_dish.encode()), (1<<16)+1, prod(salt))%salt[i], pepper%(salt[i]-1), salt[i])
    tasty_dish.append(salted_and_peppered)
shuffle(tasty_dish) # Thoroughly mix the soup after adding the condiments

[print(ltb(t).hex()+'\n'+ltb(s).hex()) for t, s in zip(tasty_dish, salt)] # Finally, serve the soup
# Bon appétit

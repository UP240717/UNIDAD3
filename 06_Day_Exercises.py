#Level1

#1
empty_tuble = ()

#2
bros = ('Julio', 'Pepe')
sis = ('Juanita', 'Mary')

#3
sibling = bros + sis
print(sibling)

#4
print('How many siblings do you have?')
print(f"I have {len(sibling)} siblings")

#5
family_members = sibling + ("Diego","Margarita")
print(family_members)

#Level2

#1
sibling = family_members[:len(sibling)]
parents = family_members[-2:]
print('Silbings: ', sibling, 'Parents: ', parents)

#2
fruit = ("Mango", "Banana", "Grape")
veggies = ("Carrot", "Onion", "Potato")
animal_product = ("Bacon", "Egg", "Butter")

food_stuff_tp = fruit + veggies + animal_product
print(food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4
mid = int(len(food_stuff_tp)/2)
food_stuff_t = food_stuff_tp[:mid]
print(food_stuff_t)

food_stuff_t2 = food_stuff_tp[mid:]
print(food_stuff_t2)

#5
first = food_stuff_lt[0:3]
print(first)

last = food_stuff_lt[-3:]
print(last)

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)




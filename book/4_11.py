my_pizzas = ["Neapolitan", "Chicago", "Margherita"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Sirnaya")
friend_pizzas.append("S more produktami")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
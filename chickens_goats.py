Heads = int(input("No. of heads = "))
Legs = int(input("No. of legs = "))
Chickens = (Legs) - 2 * (Heads)
Chickens = Chickens / 2
    
print("Goats =", Chickens)
print("Chickens =", Heads - Chickens)
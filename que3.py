qty=int(input('Qty = '))
cost=qty*100
if cost>1000:
    cost=cost-(0.1*cost) 
print("cost = ",cost)
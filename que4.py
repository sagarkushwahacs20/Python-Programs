salary=int(input('enter salary = ')) 
year=int(input('enter year of service = ')) 
if year>5:
    bonus=(salary*(5/100)) 
    print('salary after bonus- ',bonus)
else:
    print('No bonus')
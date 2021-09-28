a=int(input('Age of first person = '))
b=int(input('Age of second person = ')) 
c=int(input('Age of third person = '))
if a>b and a>c:
    print('first person is oldest- ',a)
elif b>a and b>c:
    print('second person is oldest- ',b)
elif c>a and c>b:
    print('third person is oldest- ',c)
if a<b and a<c:
    print('first person is youngest- ',a)
elif b<a and b<c:
    print('second person is youngest- ',b)
elif c<a and c<b:
    print('third person is youngest- ',c)

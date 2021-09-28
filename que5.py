a=int(input('enter phy. = '))
b=int(input('enter chem. = '))
c=int(input('enter maths = '))
d=int(input('enter eng. = '))
e=int(input('enter hindi = '))
x=(a+b+c+d+e)/5
if 80<x<100: 
    print('A')
elif 60<x<80:
    print('B') 
elif 40<x<60:
    print('C') 
else:
    print('Try Again')
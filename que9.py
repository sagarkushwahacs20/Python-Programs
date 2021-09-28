held=int(input('no of classes held = '))
attend=int(input('no of classes attend = '))
cause=input('Have you any medical cause. If Yes print y if not then print n.= ')
x=(attend/held)*100
print('x = ',x)
if x>=75 and cause=='n':
    print('Student is allowed')
elif (x<75) or cause=='y':
    print('Student is not allowed')
else:
    print('Student is not allowed')

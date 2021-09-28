held=int(input('no of classes held = '))
attend=int(input('no of classes attend = '))
x=(attend/held)*100
if x<75:
    print('Student is not allowed')
else:
    print('Student is allowed')

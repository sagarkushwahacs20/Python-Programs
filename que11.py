age=int(input('Enter age = '))
sex=input('Enter M for Male or F for Female = ')
status=(input('Enter your martial status. if married print y if not print n.= '))
if sex=='f':
    print('She will work in Urban Area')
elif sex=='m' and 20<age>40:
    print('He may work anywhere') 
elif sex=='m' and 40<age>60:
    print('He may work in Urban Area only')
else:
    print('ERROR')



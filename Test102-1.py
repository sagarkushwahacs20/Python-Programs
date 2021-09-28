def si(p=100,r=0.04,t=1):
    pro = p*r*t
    print(pro/100)

print("Press 1 to enter the principal"
      "Press 2 to enter the principal and rate"
      "Press 3 to enter the principal, rate and time")
choice = int(input())
if choice==1:
    n = float(input("Enter the principal"))
    si(n)
elif choice==2:
    n = float(input("Enter the principal"))
    m = float(input("Enter the rate"))
    si(n,m)
elif choice==3:
    n = float(input("Enter the principal"))
    m = float(input("Enter the rate"))
    o = float(input("Enter the time"))
    si(n,m,o)
else:
    print("The si with default value is ")
    si()

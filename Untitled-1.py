from function import inputnum

f=""

while f!="нет":
    try:
        s = input("Знак (+,-,*,/): ")
        if s in ('+', '-', '*', '/'):
            x = inputnum("x")
            y = inputnum("y")
            if s == '+':
                print("%.2f" % (x+y))
            elif s == '-':
                print("%.2f" % (x-y))
            elif s == '*':
                print("%.2f" % (x*y))
            elif s == '/':
                print("%.2f" % (x/y))
        print("Еще?(да/нет)")
        f=input()
    except:
            print("не надо так cksi")
            


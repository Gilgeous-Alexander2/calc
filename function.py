
def inputnum(r):
    try:
        return float(input(r+"="))
    except:
        print("Переделывай")
        return inputnum(r)
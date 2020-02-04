while True:
    w = input("Enter comma separated number: ")
    try:
        if len(w) < 2:
            raise Exception
        w = w.split(',')
        odd = [i for i in w if int(i)%2!=0]
        break
    except Exception:
        print("At least 2 numbers")
    except:
        print("There was an error")

print(','.join(odd))
        

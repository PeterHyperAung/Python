names = []
count = 0
q = ""
while True:
    a = input("Add Item > ").upper()
    q = input("Quit? > ").upper()
    names.append(a)
    if q == "YES":
        s = input("Starts > ").upper()
        for name in names:
            count += 1
            if name.startswith(s):
                print("Found the item in No." + str(count))
                break
        else:
            print("Not Found")
        break
    elif q == "NO":
        continue
    else:
        print("Out of Options")
        break

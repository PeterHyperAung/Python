cal = 'How do you want to calculate? add,subtract,multiply and divide'

while True:
    print(cal)
    type = input('')
    if type == "add":
        first = int(input('The first number> '))
        second = int(input('The second number> '))
        print(int(first + second))
        yorn = input('continue?Yes or No> ')
        if yorn == "no":
            print('Hope to meet you again')
            break
    elif type == "subtract":
        first = int(input('The first number> '))
        second = int(input('The second number> '))
        print(int(first - second))
        yorn = input('continue?Yes or No> ')
        if yorn == "no":
            print('Hope to meet you again')
            break
    elif type == "multiply":
        first = int(input('The first number> '))
        second = int(input('The second number> '))
        print(int(first * second))
        yorn = input('continue?Yes or No> ')
        if yorn == "no":
            print('Hope to meet you again')
            break
    elif type == "divide":
        first = int(input('The first number> '))
        second = int(input('The second number> '))
        print(int(first / second))
        yorn = input('continue?Yes or No> ')
        if yorn == "no":
            print('Hope to meet you again')
            break
    else:
        print('Please Choose add,subtract,multipy or divide')
